from sqlalchemy import Column, Integer, String, Text
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer)
    name = Column(String(50))
    gender = Column(String(20))
    height = Column(Integer)
    weight = Column(Integer)
    goal = Column(String(50))
    activity = Column(String(50))
    diet = Column(String(50))
    allergies = Column(String(200))
    equipment = Column(String(20))
    time_available = Column(String(50))


class Progress(Base):
    __tablename__ = "progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    date = Column(String(20))
    meals = Column(Text)
    workout = Column(Text)
    water = Column(Integer)
    steps = Column(Integer)
