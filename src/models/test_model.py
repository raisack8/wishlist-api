from sqlalchemy import Column, Integer, String

from .database import Base, engine

class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    description = Column(String, index=True)

Base.metadata.create_all(bind=engine)
