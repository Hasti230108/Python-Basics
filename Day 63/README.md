# Day 63 — Emergency Response System with Routing API

Today I upgraded my **Emergency Response System** by integrating a real-world routing API.

Previously, the system used manually defined distances between locations. Today, I replaced that approach with **OpenRouteService/HeiGIT Directions API**, which calculates actual road distance and estimated travel time between an ambulance and an emergency location.

This made the project more realistic and helped me understand how Python applications can communicate with external APIs.

## Topics Covered

* External APIs in Python
* HTTP POST requests
* `requests` library
* API authentication using an API key
* Environment variables
* `.env` files
* `python-dotenv`
* JSON API responses
* Extracting nested JSON data
* Distance conversion
* Time conversion
* API-based route calculation
* OOP integration with APIs
* Nearest ambulance selection
* Dynamic ambulance assignment
* Status management

## 1. Routing API Integration

The project uses the OpenRouteService/HeiGIT Directions API to calculate routes.

The API receives:

* Starting location coordinates
* Emergency location coordinates

and returns information such as:

* Road distance
* Estimated travel duration
* Route details

The API endpoint used in the project is:

```text
https://api.heigit.org/openrouteservice/v2/directions/driving-car
```

## 2. API Key Security

The API key is stored in a `.env` file instead of directly inside the Python source code.

The key is loaded using:

```python
from dotenv import load_dotenv
```

and:

```python
load_dotenv()

api_key = os.getenv("ORS_API_KEY")
```

The `.env` file is added to `.gitignore` so the API key is not uploaded to GitHub.

## 3. Location Coordinates

The system stores coordinates for the locations used by ambulances and emergencies.

Example:

```python
locations = {
    "Dadar": [72.8377, 19.0186],
    "Sion": [72.8530, 19.0469],
    "Bandra": [72.8407, 19.0596],
    "Andheri": [72.8479, 19.1197],
    "Kurla": [72.8794, 19.0728],
    "Powai": [72.9058, 19.1176],
    "Worli": [72.8175, 19.0178]
}
```

The coordinates are stored as:

```text
[longitude, latitude]
```

## 4. Getting Route Information

A method named `get_route_info()` sends the ambulance and emergency coordinates to the API.

```python
def get_route_info(self, amb_location, emgy_location):
```

The method:

1. Finds the coordinates.
2. Sends a POST request.
3. Receives the JSON response.
4. Extracts distance and duration.
5. Converts them into kilometers and minutes.

Distance conversion:

```python
distance_km = distance / 1000
```

Time conversion:

```python
duration_minutes = duration / 60
```

## 5. Finding the Nearest Ambulance

The system checks every ambulance whose status is:

```text
Available
```

For each available ambulance, the routing API calculates the road distance to the emergency location.

The system compares the distances and selects the ambulance with the shortest route.

Example:

```text
Bandra → Sion
Distance: 2.56 km
Estimated Time: 5.77 minutes
```

The selected ambulance is then returned from the method.

## 6. Dynamic Ambulance Assignment

The `assign_ambulance()` method was improved so that it no longer simply chooses the first available ambulance.

Instead:

```text
Emergency
    ↓
Find available ambulances
    ↓
Calculate routes using API
    ↓
Compare distances
    ↓
Find nearest ambulance
    ↓
Assign ambulance
    ↓
Change status to Busy
```

For example:

```text
Ambulance 102 assigned to Emergency 203
Emergency: Fire Injury
Location: Sion
Driver: Sameer Khan
Ambulance Status: Busy
```

## 7. Status Management

Ambulances have two main statuses:

```text
Available
Busy
```

When an ambulance is assigned:

```python
nearest_ambulance.status = "Busy"
```

This prevents the same ambulance from being selected again while it is busy.

For example, after Ambulance 102 was assigned, the system selected another available ambulance for the next search.

## Ambulance Data

The system currently contains 6 ambulances:

| ID  | Driver       | Location | Status    |
| --- | ------------ | -------- | --------- |
| 101 | Arjun Mehta  | Dadar    | Available |
| 102 | Sameer Khan  | Bandra   | Available |
| 103 | Rohan Desai  | Andheri  | Busy      |
| 104 | Vikram Joshi | Kurla    | Available |
| 105 | Jenil Shah   | Powai    | Available |
| 106 | Kunal Verma  | Worli    | Busy      |

## Emergency Data

The system currently contains 6 emergencies:

| ID  | Emergency         | Priority | Location |
| --- | ----------------- | -------- | -------- |
| 201 | Road Accident     | High     | Kurla    |
| 202 | Chest Pain        | Critical | Powai    |
| 203 | Fire Injury       | Medium   | Sion     |
| 204 | Breathing Problem | High     | Worli    |
| 205 | Traffic Accident  | Critical | Andheri  |
| 206 | Medical Emergency | Low      | Bandra   |

## API Testing

A separate file named `api_test.py` was created to test the routing API independently before integrating it into the main project.

The test successfully returned:

```text
Status Code: 200
```

Example route result:

```text
Distance: 5.43 km
Estimated Time: 7.72 minutes
```

This confirmed that the API connection was working correctly before integration.

## Technologies Used

* Python
* Object-Oriented Programming
* `requests`
* `python-dotenv`
* OpenRouteService/HeiGIT Directions API
* JSON
* Git & GitHub

## Key Takeaways

> APIs allow Python programs to communicate with external services.

> API keys should never be exposed publicly.

> JSON responses can contain deeply nested data that can be accessed using Python dictionaries and lists.

> Real road distance can be more useful than manually calculated distance for route-based applications.

> OOP can be combined with APIs to build more realistic applications.

> Changing an object's state can affect future decisions in the system.