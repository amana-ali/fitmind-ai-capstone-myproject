🧠 Fitness & Diet AI Backend

An AI-powered personal trainer that generates diet plans, workout routines, tracks user progress, and provides weekly summaries.
Built using FastAPI, MySQL, and GitHub Models (OpenAI).

🚀 Features

📋 User Registration

🥗 AI-generated Diet Plans

🏋️ AI-generated Workout Routines

📈 Daily Habit & Progress Logging

🔁 Weekly Fitness Summary by AI

💾 MySQL Database Storage

⚡ Lightning-fast FastAPI backend

🤖 Powered by GitHub LLMs (openai/gpt-4.1-mini)

🧰 Tech Stack

Python 3.10+

FastAPI

SQLAlchemy ORM

MySQL (Port 3306)

PyMySQL

GitHub Models (OpenAI API compatibility)

📦 Installation
1️⃣ Clone the repo
git clone https://github.com/yourusername/fitness-ai-backend.git
cd fitness-ai-backend

2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # macOS/Linux

3️⃣ Install dependencies
pip install -r requirements.txt

🛢 Setup MySQL Database (Port 3306)
1️⃣ Create MySQL database:
CREATE DATABASE fitness_ai;

2️⃣ Update credentials in database.py:
MYSQL_USER = "root"
MYSQL_PASSWORD = "yourpassword"
MYSQL_HOST = "localhost"
MYSQL_PORT = 3306
MYSQL_DB = "fitness_ai"

🔑 Environment Variables

Set your GitHub Models token:

Windows (PowerShell):
setx GITHUB_TOKEN "your_token_here"

▶️ Running the Server

Start FastAPI using Uvicorn:

python -m uvicorn main:app --reload


Open Swagger UI:

http://127.0.0.1:8000/docs

📡 API Endpoints (Usage Flow)
1️⃣ Register User

Creates new user and returns user_id.

POST /register

Request Body:
{
  "name": "John",
  "age": 25,
  "gender": "male",
  "height": 175,
  "weight": 72,
  "goal": "muscle gain",
  "activity": "moderate",
  "diet": "non-veg",
  "allergies": "",
  "equipment": "gym",
  "time_available": "60 min"
}

2️⃣ Generate Plan

Creates a personalized diet + workout plan.

POST /generate-plan/{user_id}

No request body required.

3️⃣ Log Daily Progress

POST /log-progress

Request Body:
{
  "user_id": 1,
  "date": "2025-11-29",
  "meals": "Eggs and oats, rice chicken",
  "workout": "Push day - bench, shoulder press",
  "water": 2500,
  "steps": 8000
}

4️⃣ Weekly Review

Analyzes logged habits & workouts.

GET /weekly-review/{user_id}

📁 Project Structure
fitness_ai_backend/
│── main.py
│── database.py
│── models.py
│── schemas.py
│── requirements.txt
│── README.md

🤖 How AI Works in This Project

The backend uses GitHub Models (OpenAI compatible):

endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-mini"


LLM generates:

calorie goals

macros

diet plans

workout routines

weekly summaries

🧪 Testing With Postman

You can test all APIs using:

http://localhost:8000/docs


or import a Postman collection (I can generate one for you).

🚀 Future Enhancements

User authentication (JWT)

Progress graphs & charts

Frontend (React / Next.js / Flutter)

Calories auto-calculation

Exercise database

Meal database

AI-based food image recognition

❤️ Contributing

PRs and feature requests are welcome!