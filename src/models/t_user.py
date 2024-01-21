from sqlalchemy import Column, Integer, String, DateTime
from .base import OrgBaseModel
from .database import Base, engine

class TUser(Base, OrgBaseModel):
    __tablename__ = "t_user"

    uuid = Column(String, nullable=False, index=True, primary_key=True)
    sub = Column(String, nullable=False, index=True, unique=True)
    name = Column(String, nullable=False, index=True)
    picture = Column(String, nullable=False, index=True)
    last_login_at = Column(DateTime, nullable=True, index=True)
    gender = Column(Integer, index=True)
    first_page_id = Column(String, index=True)
    # userテーブル定義について要検討

Base.metadata.create_all(bind=engine)