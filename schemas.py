from pydantic import BaseModel


class UserInfo(BaseModel):
    age: int
    name: str
    gender: str
    height: int
    weight: int
    goal: str
    activity: str
    diet: str
    allergies: str = ""
    equipment: str = "home"
    time_available: str = "30 min"

    class Config:
        orm_mode = True


class HabitLog(BaseModel):
    user_id: int
    date: str
    meals: str = ""
    workout: str = ""
    water: int = 0
    steps: int = 0

    class Config:
        orm_mode = True
