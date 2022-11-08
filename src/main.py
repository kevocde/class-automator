from datetime import timedelta, datetime
from decouple import config
from fastapi import FastAPI, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
from .rest import BasicUserInfo
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

    for i in range(30):
        current = start + timedelta(days=i)
        if int(current.strftime("%w")) != 0:
            pieces = [current.strftime("%m"), current.strftime("%d"), current.strftime("%Y")]
            dates.append('/'.join([str(int(value)) for value in pieces]))

    return {"datesEnabled": dates}

    # dates = [(start + timedelta(days=i)) for i in range(30)]
    # dates = filter(lambda date: date.strftime("%w") != 1, dates)
    # return {"dates-enabled": [date.strftime("%m/%d/%Y") for date in dates]}
