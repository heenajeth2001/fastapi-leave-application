from pydantic import BaseModel,root_validator,validator
from datetime import date

class LeaveList(BaseModel):
    id : int
    start_date : date
    end_date : date
    status : int
    reason : str

    class Config:
        orm_mode = True

class CreateLeave(BaseModel):
    start_date : date
    end_date : date
    reason : str

    @root_validator
    def verify_date(cls,values):
        if values['start_date'] > values['end_date']:
            raise ValueError("start_date should be less than end_date.")
        return values

    # @validator("start_date")
    # def verify_date(cls,values):
    #     pass