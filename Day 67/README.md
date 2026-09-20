# Day 67 — Emergency Search

Today I continued working on my **Emergency Response System** project.

I added an emergency search feature that allows the system to find an emergency using its ID.

## Topics Covered

* Searching objects using IDs
* Loops and conditions
* Object attributes
* OOP method implementation
* Emergency data retrieval
* Handling invalid IDs

## Emergency Search

Added the `search_emergency()` method:

```python
def search_emergency(self, emgy_id):
    for emgy in self.multiple_emgy:
        if emgy_id == emgy.emgy_id:
            print("\n==== EMERGENCY FOUND ====")
            print(f"Emergency ID: {emgy.emgy_id}")
            print(f"Emergency: {emgy.what_emgy}")
            print(f"Priority: {emgy.how_much_urgent}")
            print(f"Location: {emgy.emgy_location}")
            return

    print("\nEmergency ID not found!")
```

## Testing

```python
system.search_emergency(202)
system.search_emergency(999)
```

The system successfully found Emergency `202` and correctly handled an invalid Emergency ID.

## Project Features So Far

* Ambulance Management
* Emergency Management
* Priority-Based Dispatch
* Nearest Ambulance Selection
* Routing API Integration
* Ambulance Status Updates
* Emergency Completion
* Available Ambulance Tracking
* Emergency Search

## Technologies Used

* Python
* OOP
* `heapq`
* `requests`
* `python-dotenv`
* OpenRouteService API

## Key Takeaway

I practiced searching through a list of objects and accessing their attributes using an ID.