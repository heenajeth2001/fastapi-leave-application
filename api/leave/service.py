from models import Leave
from utils.constant import PENDING
from fastapi.exceptions import HTTPException

async def get_leaves_list(db,user):
    leave_list = db.query(Leave).filter(Leave.user_id == user.id).order_by(Leave.id).all()
    return leave_list

async def create_leave(db,user,leave_request):
    leave_request_exists = db.query(Leave).filter(Leave.start_date == leave_request.start_date,
                                                  Leave.end_date == leave_request.end_date,
                                                  Leave.user_id == user.id
                                                  ).first()

    if leave_request_exists:    
        raise HTTPException(status_code=400,detail="Leave Request already exists.")

    create_leave_request = Leave(
                            start_date=leave_request.start_date, 
                            end_date=leave_request.end_date, 
                            user_id=user.id,
                            reason=leave_request.reason,
                            status = PENDING
                        )
    db.add(create_leave_request)
    db.commit()
    db.refresh(create_leave_request)
    return create_leave_request