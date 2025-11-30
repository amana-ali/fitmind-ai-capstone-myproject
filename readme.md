# FitMindAI – Fitness & Diet AI Backend

An AI-powered wellness backend that generates personalized workout routines, diet plans, habit tracking, and weekly fitness summaries.  
Built with FastAPI, MySQL, and GitHub Models (OpenAI-compatible).

---

## Features

- User registration  
- AI-generated diet plans  
- AI-generated workout routines  
- Daily habit and progress logging  
- Weekly AI-powered fitness summaries  
- MySQL database storage  
- FastAPI backend  
- Powered by GitHub Models (OpenAI / GPT-compatible)

---

## Tech Stack

- Python 3.10+  
- FastAPI  
- SQLAlchemy ORM  
- MySQL  
- PyMySQL  
- GitHub Models (OpenAI-compatible)

---

## Installation

```bash
git clone https://github.com/amana-ali/fitmind-ai-capstone-myproject.git  
cd fitmind-ai-capstone-myproject
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

- On Windows:
  ```bash
  venv\Scripts\activate
  ```
- On macOS / Linux:
  ```bash
  source venv/bin/activate
  ```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Database Setup (MySQL — Port 3306)

1. Create the database:

```sql
CREATE DATABASE fitness_ai;
```

2. Update the credentials in `database.py`:

```python
MYSQL_USER = "root"
MYSQL_PASSWORD = "yourpassword"
MYSQL_HOST = "localhost"
MYSQL_PORT = 3306
MYSQL_DB = "fitness_ai"
```

---

## Environment Variables

Set your GitHub Models token:

- On Windows (PowerShell):

  ```powershell
  setx GITHUB_TOKEN "your_token_here"
  ```

- On macOS / Linux:

  ```bash
  export GITHUB_TOKEN="your_token_here"
  ```

---

## Running the Server

Start the FastAPI server using Uvicorn:

```bash
python -m uvicorn main:app --reload
```

Open the API documentation at:  
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## API Endpoints

### 1. Register User  
**POST** `/register`  
Request body example:
```json
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
```

### 2. Generate Plan  
**POST** `/generate-plan/{user_id}`  
Generates personalized diet and workout plan.

### 3. Log Daily Progress  
**POST** `/log-progress`  
Request body example:
```json
{
  "user_id": 1,
  "date": "2025-11-29",
  "meals": "Eggs and oats, rice chicken",
  "workout": "Push day - bench, shoulder press",
  "water": 2500,
  "steps": 8000
}
```

### 4. Weekly Review  
**GET** `/weekly-review/{user_id}`  
Generates weekly summary and suggestions based on logged data.

---

## Project Structure

```
fitmind-ai-capstone-myproject/
│── main.py  
│── database.py  
│── models.py  
│── schemas.py  
│── requirements.txt  
│── README.md  
```

---

## How AI Works

The backend uses GitHub Models (OpenAI-compatible):

```python
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-mini"
```

The model generates:
- Calorie targets  
- Macronutrient breakdowns  
- Complete meal plans  
- Workout routines  
- Weekly summaries and suggestions based on user logs  

---

## Testing

After running the server, you can test all APIs via Swagger UI at:  
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Future Enhancements

- JWT-based user authentication  
- Progress tracking charts & analytics  
- Frontend interface (React / Next.js / Flutter)  
- Automatic calorie calculation & nutrition database  
- Expanded exercise & meal databases  
- AI-based food image recognition  

---

## Notes

This project was developed as part of my Kaggle Capstone submission.





