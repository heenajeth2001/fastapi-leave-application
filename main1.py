from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()
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