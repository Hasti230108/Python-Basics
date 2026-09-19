import os 
import requests 
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ORS_API_KEY")

url = "https://api.heigit.org/openrouteservice/v2/directions/driving-car"

headers = {
    "Authorization": api_key,
    "Content-Type": "application/json"
}

data = {
    "coordinates": [
        [72.8377, 19.0186],
        [72.8530, 19.0469]
    ]
}

response = requests.post(url, json=data, headers=headers)

print("Status Code:", response.status_code)
print("Reponse:")

result = response.json()

distance = result["routes"][0]["summary"]["distance"]
duration = result["routes"][0]["summary"]["duration"]

distance_km = distance / 1000
duration_minutes = duration / 60

print("Distance:", round(distance_km, 2), "km")
print("Estimated Time:", round(duration_minutes, 2), "minutes")