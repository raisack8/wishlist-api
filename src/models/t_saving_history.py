from sqlalchemy import Column, Integer, String
from .base import OrgBaseModel
from .database import Base, engine

class TSavingHistory(Base, OrgBaseModel):
    __tablename__ = "t_saving_history"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    amount = Column(Integer, nullable=False, index=True)
    group_id = Column(String, index=True) # uuid
    user_id = Column(String, index=True) # uuid

Base.metadata.create_all(bind=engine)