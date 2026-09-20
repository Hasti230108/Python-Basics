import heapq

priority_queue = []

emergencies = [
    (2, 201, "Road Accident", "Kurla"),
    (1, 202, "Chest Pain", "Powai"),
    (3, 203, "Fire Injury", "Sion"),
    (2, 204, "Breathing Problem", "Worli"),
    (1, 205, "Traffic Accident", "Andheri"),
    (4, 206, "Medical Emergency", "Bandra")
]

for emergency in emergencies:
    heapq.heappush(priority_queue, emergency)

print("\n==== PRIORITY QUEUE ==== ")
while priority_queue:
    priority, emgy_id, emgy_description, emgy_location = heapq.heappop(priority_queue)

    print(f"Emergency ID: {emgy_id}")
    print(f"Emergency: {emgy_description}")
    print(f"Priority: {priority}")
    print(f"Location: {emgy_location}")
    print()