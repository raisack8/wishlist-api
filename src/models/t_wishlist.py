from sqlalchemy import Column, Integer, String, DateTime
from .base import OrgBaseModel
from .database import Base, engine


class TWishlist(Base, OrgBaseModel):
    __tablename__ = "t_wishlist"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    uuid = Column(String, index=True, nullable=False)
    title = Column(String, index=True, nullable=False)
    category = Column(String, index=True, nullable=True)
    price = Column(Integer, nullable=True, index=True)
    image_url = Column(String, nullable=True, index=True)
    group_id = Column(String, nullable=True, index=True)
    user_id = Column(String, nullable=True, index=True)
    purchased_at = Column(DateTime, nullable=True, index=True)
    memo = Column(String, nullable=True, index=True)
    wish_rank = Column(Integer, nullable=True, index=True)


Base.metadata.create_all(bind=engine)
