from fastapi import APIRouter,Request,Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from db.deps import get_db,get_current_user
from models import User,Leave
from .service import get_leaves_list,create_leave
from .schema import LeaveList,CreateLeave

templates = Jinja2Templates(directory="templates")
leave_router = APIRouter()

@leave_router.get("/",include_in_schema=False)
async def Index(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})

@leave_router.get("/leaves",response_model=list[LeaveList])
async def get_leaves(db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    return await get_leaves_list(db,current_user)

@leave_router.post("/leaves/create",response_model=LeaveList)
async def create_leaves(leave: CreateLeave, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return await create_leave(db, current_user, leave)

