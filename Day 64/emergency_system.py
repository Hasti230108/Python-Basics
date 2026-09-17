import os
import requests
from dotenv import load_dotenv
import heapq

load_dotenv()

api_key = os.getenv("ORS_API_KEY")

class Ambulance:
    def __init__(self, amb_id, driver_name, current_loc, status):
        self.amb_id = amb_id
        self.driver_name = driver_name
        self.current_loc = current_loc
        self.status = status

    def display_ambulance(self):
        print(f"Ambulance ID: {self.amb_id}")
        print(f"Driver Name: {self.driver_name}")
        print(f"Current Location: {self.current_loc}")
        print(f"Status: {self.status}\n")

class Emergency:
    def __init__(self, emgy_id, what_emgy, how_much_urgent, emgy_location):
        self.emgy_id = emgy_id
        self.what_emgy = what_emgy
        self.how_much_urgent = how_much_urgent
        self.emgy_location = emgy_location

    def display_emergency(self):
        print(f"Emergency ID: {self.emgy_id}")
        print(f"What Emergency: {self.what_emgy}")
        print(f"How Much Urgent: {self.how_much_urgent}")
        print(f"Emergency Location: {self.emgy_location}\n")

class EmergencySystem:
    locations = {
        "Dadar": [72.8377, 19.0186],
        "Sion": [72.8530, 19.0469],
         "Bandra": [72.8407, 19.0596],
        "Andheri": [72.8479, 19.1197],
        "Kurla": [72.8794, 19.0728],
        "Powai": [72.9058, 19.1176],
        "Worli": [72.8175, 19.0178]
        }

    priority = {
            "Critical": 4,
            "High": 3,
            "Medium": 2,
            "Low": 1
        }

    def __init__(self):
        self.multiple_amb = []
        self.multiple_emgy = []
        self.priority_queue = []

    def add_ambulance(self, amb_id, driver_name, current_loc, status):
        new_ambulance = Ambulance(amb_id, driver_name, current_loc, status)
        self.multiple_amb.append(new_ambulance)

    def add_emergency(self, emgy_id, what_emgy, how_much_urgent, emgy_location):
        new_emergency = Emergency(emgy_id, what_emgy, how_much_urgent, emgy_location)
        self.multiple_emgy.append(new_emergency)

    def add_to_priority_queue(self):
        for emgy in self.multiple_emgy:
            priority = 5 - self.priority[emgy.how_much_urgent]

            heapq.heappush(
                self.priority_queue,
                (
                    priority,
                    emgy.emgy_id,
                    emgy.what_emgy,
                    emgy.emgy_location
                )
            )

    def process_priority_queue(self):
        while self.priority_queue:
            priority, emgy_id, emgy_description, emgy_location = heapq.heappop(
                self.priority_queue
            )

            print("\n===== PROCESSING EMERGENCY =====")
            print(f"Emergency ID: {emgy_id}")
            print(f"Emergency: {emgy_description}")
            print(f"Location: {emgy_location}")

            self.assign_ambulance(emgy_id)

    def display_ambulances(self):
        for ambulance in self.multiple_amb:
            ambulance.display_ambulance()

    def display_emergencies(self):
        for emergency in self.multiple_emgy:
            emergency.display_emergency()

    def get_route_info(self, amb_location, emgy_location):
        start = self.locations.get(amb_location)
        end = self.locations.get(emgy_location)

        if start is None or end is None:
            print("Location coordinates not found!")
            return None

        url = "https://api.heigit.org/openrouteservice/v2/directions/driving-car"

        headers = {
            "Authorization": api_key,
            "Content-Type": "application/json"
        }

        data = {
            "coordinates": [start,end]
        }

        response = requests.post(url, json=data, headers=headers)

        if response.status_code != 200:
            print("API request failed!")
            return None

        result = response.json()

        distance = result["routes"][0]["summary"]["distance"]
        duration = result["routes"][0]["summary"]["duration"]

        distance_km = distance / 1000
        duration_minutes = duration / 60

        return distance_km, duration_minutes

    def find_highest_priority_emergency(self):
        if not self.multiple_emgy:
            print("No emergencies available!")
            return

        highest_priority = None

        for emgy in self.multiple_emgy:
            if highest_priority is None:
                highest_priority = emgy
            elif self.priority[emgy.how_much_urgent] > self.priority[highest_priority.how_much_urgent]:
                highest_priority = emgy

        print("\n===== HIGHEST PRIORITY EMERGENCY =====")
        print(f"Emergency ID: {highest_priority.emgy_id}")
        print(f"Emergency: {highest_priority.what_emgy}")
        print(f"Priority: {highest_priority.how_much_urgent}")
        print(f"Location: {highest_priority.emgy_location}")

    def find_nearest_ambulance(self, emgy_location):
        nearest_ambulance = None
        shortest_distance = None
        shortest_duration = None

        for amb in self.multiple_amb:
            if amb.status == "Available":
                route_info = self.get_route_info(
                    amb.current_loc,
                    emgy_location
                )

                if route_info is not None:
                    distance, duration = route_info

                    if shortest_distance is None or distance < shortest_distance:
                        shortest_distance = distance
                        shortest_duration = duration
                        nearest_ambulance = amb

        if nearest_ambulance is not None:
            print("\n===== NEAREST AVAILABLE AMBULANCE =====")
            print(f"Ambulance ID: {nearest_ambulance.amb_id}")
            print(f"Driver: {nearest_ambulance.driver_name}")
            print(f"Current Location: {nearest_ambulance.current_loc}")
            print(f"Emergency Location: {emgy_location}")
            print(f"Distance: {round(shortest_distance, 2)} km")
            print(f"Estimated Time: {round(shortest_duration, 2)} minutes")

            return nearest_ambulance
        else:
            print("\nNo suitable ambulance found!")

    def assign_ambulance(self, emgy_id):
        emergency_found = False

        for emgy in self.multiple_emgy:
            if emgy.emgy_id == emgy_id:
                emergency_found = True

                nearest_ambulance = self.find_nearest_ambulance(
                    emgy.emgy_location
                )

                if nearest_ambulance is not None:
                    nearest_ambulance.status = "Busy"

                    print(f"\nAmbulance {nearest_ambulance.amb_id} assigned to Emergency {emgy.emgy_id}")
                    print(f"Emergency: {emgy.what_emgy}")
                    print(f"Location: {emgy.emgy_location}")
                    print(f"Driver: {nearest_ambulance.driver_name}")
                    print(f"Ambulance Status: {nearest_ambulance.status}")
                else:
                    print("\nNo available ambulance!")
                return

        if not emergency_found:
            print(f"\nEmergency ID {emgy_id} not found!") 

system = EmergencySystem()

system.add_ambulance(101, "Arjun Mehta", "Dadar", "Available")
system.add_ambulance(102, "Sameer Khan", "Bandra", "Available")
system.add_ambulance(103, "Rohan Desai", "Andheri", "Busy")
system.add_ambulance(104, "Vikram Joshi", "Kurla", "Available")
system.add_ambulance(105, "Jenil Shah", "Powai", "Available")
system.add_ambulance(106, "Kunal Verma", "Worli", "Busy")

system.add_emergency(201, "Road Accident", "High", "Kurla")
system.add_emergency(202, "Chest Pain", "Critical", "Powai")
system.add_emergency(203, "Fire Injury", "Medium", "Sion")
system.add_emergency(204, "Breathing Problem", "High", "Worli")
system.add_emergency(205, "Traffic Accident", "Critical", "Andheri")
system.add_emergency(206, "Medical Emergency", "Low", "Bandra")

print("===== AMBULANCES =====")
system.display_ambulances()

print("===== EMERGENCIES =====")
system.display_emergencies()

print("\n==== PRIORITY DISPATCH ====")
system.add_to_priority_queue()
system.process_priority_queue()