import locale
import random
import asyncio
import time
from datetime import timedelta, datetime
from decouple import config
from fastapi import FastAPI, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
from .rest import repositories, BasicUserInfo, ClassDetails, Schedule, POSSIBLE_MESSAGUES
from .moodle import Api
from fastapi_utils.tasks import repeat_every

locale.setlocale(locale.LC_ALL, 'es_CO.UTF-8')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=config("ALLOW_ORIGINS").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Welcome to Class Automator system"}


@app.post("/user-information")
async def check_login(data: BasicUserInfo):
    data.platform = config("ACADEMY_URL")
    api = Api(*data.to_credentials())
    try:
        api.check_credentials()
        return Response(status_code=201)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=str(ex))


@app.get("/dates-enabled")
async def get_dates_enabled():
    start = datetime.now() + timedelta(days=2)
    dates = []

    if start.time().hour > 12:
        start += timedelta(days=1)

    for i in range(30):
        current = start + timedelta(days=i)
        if int(current.strftime("%w")) != 0:
            pieces = [current.strftime("%m"), current.strftime("%d"), current.strftime("%Y")]
            dates.append('/'.join([str(int(value)) for value in pieces]))

    return {"datesEnabled": dates}


@app.post("/schedules")
async def set_schedule(user_information: BasicUserInfo, class_details: ClassDetails, schedule: Schedule):
    try:
        user_information = repositories \
            .BasicUserInfoRepository \
            .update_or_create({
            **{'student_code': class_details.student_code},
            **user_information.dict(exclude={'platform'})
        })

        if not user_information:
            raise ValueError()

        schedule = repositories \
            .SchedulesRepository \
            .create({
            **{'user_id': user_information[0]},
            **class_details.dict(exclude={'student_code'}),
            **schedule.dict()
        })

        if not schedule:
            raise ValueError()

        return Response(status_code=201)
    except Exception:
        raise HTTPException(500, "An error has occurred while scheduling the class.")


@app.on_event("startup")
@repeat_every(seconds=60)
async def execute_shedules() -> None:
    try:
        instances: dict[str, Api] = {}
        schedules_info = repositories.SchedulesRepository.find_next_shedules_to_schedule()
        for (id, schedule, attempts) in schedules_info:
            if (schedule.times - attempts) > 0:
                if id not in instances:
                    instances[id] = Api(
                        platform_url=config('ACADEMY_URL'),
                        username=schedule.user.user,
                        password=schedule.user.password
                    )

                api = instances[id]
                asyncio.create_task(process_schedule(api, schedule, attempts))
    except Exception as ex:
        print(ex)


async def process_schedule(api, schedule, attempts):
    schedule_date = datetime.strptime(schedule.date, '%Y-%m-%d') + timedelta(days=(7 * attempts))
    message = random \
        .choice(POSSIBLE_MESSAGUES) \
        .format(schedule_date.strftime('%A %d de %B'), schedule.time, schedule.get_message())
    message = api.send_message(config('DEFAULT_TO'), message)

    if message:
        times = int(config('LOOK_FOR')) // int(config('CHECK_EACH'))
        while times > 0:
            try:
                resp = api.get_response(config('DEFAULT_TO'), message[-1].timecreated)
                if resp:
                    print(resp)
                    return
                else:
                    print("May be the next time")
            finally:
                times -= 1
                time.sleep(int(config('CHECK_EACH')))
