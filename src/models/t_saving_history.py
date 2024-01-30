from sqlalchemy import Column, Integer, String
from .base import OrgBaseModel
from .database import Base, engine


class TSavingHistory(Base, OrgBaseModel):
    __tablename__ = "t_saving_history"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    uuid = Column(String, index=True, nullable=False)
    amount = Column(Integer, nullable=False, index=True)
    group_id = Column(String, index=True)
    user_id = Column(String, index=True)


Base.metadata.create_all(bind=engine)
