import os
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from openai import OpenAI

from database import Base, engine, SessionLocal
from models import User, Progress
from schemas import UserInfo, HabitLog

# Create MySQL tables
Base.metadata.create_all(bind=engine)

# LLM Configuration (GitHub Models)
TOKEN = os.environ["GITHUB_TOKEN"]
ENDPOINT = "https://models.github.ai/inference"
MODEL = "openai/gpt-4.1-mini"

client = OpenAI(base_url=ENDPOINT, api_key=TOKEN)

app = FastAPI()


# ---------------------- DB Dependency ----------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------------- API ROUTES ----------------------

@app.post("/register")
def register_user(user: UserInfo, db: Session = Depends(get_db)):
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered", "user_id": new_user.id}


@app.post("/generate-plan/{user_id}")
def generate_plan(user_id: int, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return {"error": "User not found"}

    prompt = f"""
    You are a fitness and nutrition expert AI.

    User Info:
    Age: {user.age}
    Gender: {user.gender}
    Height: {user.height}
    Weight: {user.weight}
    Goal: {user.goal}
    Activity: {user.activity}
    Diet: {user.diet}
    Allergies: {user.allergies}
    Equipment: {user.equipment}
    Time available: {user.time_available}

    Provide:
    1. Daily calories
    2. Macros
    3. 7-day diet plan
    4. 5-day workout plan
    Return JSON only.
    """

    res = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8
    )

    return {"plan": res.choices[0].message.content}


@app.post("/log-progress")
def log_progress(log: HabitLog, db: Session = Depends(get_db)):

    new_log = Progress(**log.dict())
    db.add(new_log)
    db.commit()

    return {"message": "Progress saved"}


@app.get("/weekly-review/{user_id}")
def weekly_review(user_id: int, db: Session = Depends(get_db)):

    logs = db.query(Progress).filter(Progress.user_id == user_id).all()

    if not logs:
        return {"message": "No logs found"}

    logs_text = ""
    for log in logs:
        logs_text += (
            f"Date: {log.date}, Meals: {log.meals}, Workout: {log.workout}, "
            f"Water: {log.water}, Steps: {log.steps}\n"
        )

    prompt = f"""
    You are a fitness coach AI.

    Here is the user's weekly progress:
    {logs_text}

    Provide:
    - Diet consistency
    - Workout consistency
    - Habits
    - Improvements for next week
    Keep response short and motivational.
    """

    res = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return {"summary": res.choices[0].message.content}


@app.get("/")
def root():
    return {"message": "Fitness AI Backend with MySQL is running!"}
