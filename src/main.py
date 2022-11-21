from datetime import timedelta, datetime
from decouple import config
from fastapi import FastAPI, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
from .rest import repositories, BasicUserInfo, ClassDetails, Schedule
from .moodle import Api

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
