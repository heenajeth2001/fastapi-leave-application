from sqlalchemy import Boolean, Column, Integer, String,DateTime,Date,ForeignKey
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), index=True, nullable=False)
    username = Column(String(50), index=True, nullable=False)
    password = Column(String(512), nullable=False)
    mobile = Column(String(15), nullable=True)
    firstname = Column(String(50), nullable=True)
    lastname = Column(String(50), nullable=True)
    is_active = Column(Boolean, default=True)
    leaves = relationship("Leave", back_populates="user")
    created_by = Column(Integer, nullable=True)
    updated_by = Column(Integer, nullable=True)
    created_on = Column(DateTime, default=datetime.utcnow)
    updated_on = Column(DateTime, default=datetime.utcnow)

class Leave(Base):
    __tablename__ = "leaves"
    id = Column(Integer, primary_key=True, index=True)
    start_date = Column(Date)
    end_date = Column(Date)
    reason = Column(String(50), nullable=True)
    status = Column(Integer,nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="leaves")
    updated_by = Column(Integer, nullable=True)
    created_on = Column(DateTime, default=datetime.utcnow)
    updated_on = Column(DateTime, default=datetime.utcnow)
