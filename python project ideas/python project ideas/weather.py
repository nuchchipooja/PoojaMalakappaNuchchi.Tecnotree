#import requests
import json

# Define the base URL for the OpenWeatherMap API
base_url = "https://api.openweathermap.org/data/2.5/weather"
#base_url =  "https://home.openweathermap.org/api_keys"
# Get the user's city input
city = input("Enter a city name: ")

# Set up the parameters for the API request
params = {"q": city, "appid": "e9c1553b1b2b111b91bc9430cec323bb", "units": "metric"}

# Send the API request and store the response
response = requests.get(base_url, params=params)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the response JSON data
    data = json.loads(response.text)
    # Get the current weather condition
    weather = data["weather"][0]["description"]
    # Get the temperature in Celsius
    temp = data["main"]["temp"]
    # Print the weather and temperature information
    print(f"The weather in {city.title()} is {weather} with a temperature of {temp}°C.")
else:
    # Print an error message if the request was unsuccessful
    print(f"Error: {response.status_code}")
