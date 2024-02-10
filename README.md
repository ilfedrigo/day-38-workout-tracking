# Workout Tracker Readme

38 days with Python

This Python script is designed to track workouts and store them using the Nutritionix API and Google Sheets.

## Setup

1. Obtain API credentials from Nutritionix:
   - API ID
   - API Key

2. Update the `API_ID` and `API_KEY` variables in the script with your Nutritionix API credentials.

3. Set up Google Sheets:
   - Create a Google Sheets document to store workout data.
   - Get the endpoint URLs for both reading and writing data (GET_SHEETY and POST_SHEETY).

## Usage

1. Run the script.
2. Enter the exercises you performed when prompted.
3. The script will make a request to the Nutritionix API to retrieve exercise information based on your input.
4. The retrieved exercise data will be stored in the Google Sheets document.
