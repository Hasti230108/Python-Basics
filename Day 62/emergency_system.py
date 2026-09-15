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
    priority = {
            "Critical": 4,
            "High": 3,
            "Medium": 2,
            "Low": 1
        }

    distances = {
        ("Dadar", "Sion"): 4,
        ("Bandra", "Sion"): 8,
        ("Andheri", "Sion"): 10,
        ("Dadar", "Kurla"): 7,
        ("Bandra", "Kurla"): 12,
        ("Andheri", "Kurla"): 15,
        ("Dadar", "Powai"): 12,
        ("Bandra", "Powai"): 10,
        ("Andheri", "Powai"): 8,
        ("Dadar", "Worli"): 6,
        ("Bandra", "Worli"): 5,
        ("Andheri", "Worli"): 12
    }

    def __init__(self):
        self.multiple_amb = []
        self.multiple_emgy = []

    def add_ambulance(self, amb_id, driver_name, current_loc, status):
        new_ambulance = Ambulance(amb_id, driver_name, current_loc, status)
        self.multiple_amb.append(new_ambulance)

    def add_emergency(self, emgy_id, what_emgy, how_much_urgent, emgy_location):
        new_emergency = Emergency(emgy_id, what_emgy, how_much_urgent, emgy_location)
        self.multiple_emgy.append(new_emergency)

    def display_ambulances(self):
        for ambulance in self.multiple_amb:
            ambulance.display_ambulance()

    def display_emergencies(self):
        for emergency in self.multiple_emgy:
            emergency.display_emergency()

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

        for amb in self.multiple_amb:
            if amb.status == "Available":
                distance = self.distances.get(
                    (amb.current_loc, emgy_location)
                )

                if distance is not None:
                    if shortest_distance is None or distance < shortest_distance:
                        shortest_distance = distance
                        nearest_ambulance = amb

        if nearest_ambulance is not None:
            print("\n===== NEAREST AVAILABLE AMBULANCE =====")
            print(f"Ambulance ID: {nearest_ambulance.amb_id}")
            print(f"Driver: {nearest_ambulance.driver_name}")
            print(f"Current Location: {nearest_ambulance.current_loc}")
            print(f"Emergency Location: {emgy_location}")
            print(f"Distance: {shortest_distance} km")
        else:
            print("\nNo suitable ambulance found!")

    def assign_ambulance(self, emgy_id):
        emergency_found = False

        for emgy in self.multiple_emgy:
            if emgy.emgy_id == emgy_id:
                emergency_found = True

                for amb in self.multiple_amb:
                    if amb.status == "Available":
                        amb.status = "Busy"

                        print(f"\nAmbulance {amb.amb_id} assigned to Emergency {emgy.emgy_id}")
                        print(f"Emergency: {emgy.what_emgy}")
                        print(f"Location: {emgy.emgy_location}")
                        print(f"Driver: {amb.driver_name}")
                        print(f"Ambulance Status: {amb.status}")
                        return

                print("\nNo available ambulance!")
                return

        if not emergency_found:
            print(f"\nEmergency ID {emgy_id} not found!") 

system = EmergencySystem()

system.add_ambulance(101, "Arjun Mehta", "Dadar", "Available")
system.add_ambulance(102, "Sameer Khan", "Bandra", "Available")
system.add_ambulance(103, "Rohan Desai", "Andheri", "Busy")

system.add_emergency(201, "Road Accident", "High", "Kurla")
system.add_emergency(202, "Chest Pain", "Critical", "Powai")
system.add_emergency(203, "Fire Injury", "Medium", "Sion")
system.add_emergency(204, "Breathing Problem", "High", "Worli")

print("===== AMBULANCES =====")
system.display_ambulances()

print("===== EMERGENCIES =====")
system.display_emergencies()

print("===== HIGHEST PRIORITY =====")
system.find_highest_priority_emergency()

print("\n===== FINDING NEAREST AMBULANCE =====")
system.find_nearest_ambulance("Sion")

print("\n===== ASSIGNING AMBULANCE =====")
system.assign_ambulance(203)

print("\n===== FINDING NEAREST AMBULANCE AFTER ASSIGNMENT =====")
system.find_nearest_ambulance("Sion")