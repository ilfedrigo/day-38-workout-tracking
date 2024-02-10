import requests
from datetime import datetime
import json

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

GENDER = "male"
WEIGHT_KG = 72
HEIGHT_CM = 173
AGE = 32

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
EXERCISE_TEXT = "ran about 30 minutes"

GET_SHEETY = "https://api.sheety.co/2562639edf04f0d34bec0ec17a4b4386/myWorkouts/workouts"
POST_SHEETY = "https://api.sheety.co/2562639edf04f0d34bec0ec17a4b4386/myWorkouts/workouts"

API_ID = "c6fbdd13"
API_KEY = "079c4d7c91593616e955d6f6adf7cdfa"

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
}

parameters = {
    "query": EXERCISE_TEXT,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
    }


response = requests.post(EXERCISE_ENDPOINT, json=parameters, headers=headers)
result = response.json()



for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(GET_SHEETY, json=sheet_inputs)

    print(sheet_response.text)