from fastapi.responses import JSONResponse
import models,time
from fastapi import Depends, FastAPI,Request
from utils.database import DBConnection
from api.auth.router import api_router
from api.leave.router import leave_api_router
from fastapi.templating import Jinja2Templates
from config import settings
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static",StaticFiles(directory="static"),name="static")
templates = Jinja2Templates(directory="templates")
engine = DBConnection().getEngine()

models.Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

app.include_router(api_router, prefix=settings.API_V2_STR)
app.include_router(leave_api_router)


data = [
        {
            "id" : 1,
            "startDate" : '05-08-2023',
            "endDate" : '06-12-2023',
            "reason" : 'Birthday',
            "status" : 'Pending'
        },
        {
            "id" : 2,
            "startDate" : '06-08-2023',
            "endDate" : '10-12-2023',
            "reason" : 'Birthday',
            "status" : 'Pending'
        },
        {
            "id" : 3,
            "startDate" : '12-08-2023',
            "endDate" : '20-12-2023',
            "reason" : 'Birthday',
            "status" : 'Pending'
        }
        
    ]
# data = [{},{},{},{},{},{},{},{},{},{}]
# limit=2
# page=1
# data=[[{},{}],[{},{}],[{},{}],[{},{}],[{},{}]]
# data[10-1]

@app.get("/leave-list")
async def get_leave_list():
    return data

@app.get("/leave-list/{leave_id}")
async def get_leave_by_id(skip:int=1,limit:int=10,leave_id:int | None = None):
    res = list(filter(lambda x:x['id'] == leave_id,data))
    if len(res) == 0:
        return JSONResponse(content={"msg" : "Invalid leave_id"},status_code=404)
    return res

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
    # uvicorn.main()