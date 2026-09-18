# Day 65 — Ambulance Status Update

Today I continued working on my **Emergency Response System** project.

The main goal of Day 65 was to add a simple feature for **updating the status of an ambulance**.

This allows an ambulance's status to be changed between states such as `Available` and `Busy`.

## Topic Covered

- Updating object attributes
- Searching objects inside a list
- Using `for` loops with objects
- Comparing object IDs
- Updating ambulance status
- Handling invalid ambulance IDs
- Applying OOP concepts in a real-world project

## Ambulance Status Update

A new method was added to the `EmergencySystem` class:

```python
def update_ambulance_status(self, amb_id, new_status):

    for amb in self.multiple_amb:

        if amb.amb_id == amb_id:
            amb.status = new_status

            print(
                f"Ambulance {amb_id} status updated to {new_status}"
            )

            return

    print("Ambulance ID not found!")
```

## How It Works

The method:

1. Takes an ambulance ID.
2. Takes the new status.
3. Searches through the ambulance list.
4. Finds the ambulance with the matching ID.
5. Updates its status.
6. Prints a confirmation message.
7. Displays an error if the ambulance ID does not exist.

## Test Cases

### Test 1

```python
system.update_ambulance_status(101, "Busy")
```

Output:

```text
Ambulance 101 status updated to Busy
```

### Test 2

```python
system.update_ambulance_status(105, "Available")
```

Output:

```text
Ambulance 105 status updated to Available
```

### Test 3

```python
system.update_ambulance_status(999, "Busy")
```

Output:

```text
Ambulance ID not found!
```

## Key Takeaways

> Object attributes can be changed after an object is created.

> A list of objects can be searched using a `for` loop.

> Comparing object attributes helps identify a specific object.

> Updating status dynamically makes the emergency system more realistic.

> Invalid IDs should be handled properly instead of causing errors.

## Emergency Response System Progress

The project now includes:

* Ambulance Management
* Emergency Management
* OOP Classes
* Ambulance Assignment
* Emergency Priority Levels
* Priority Queue using `heapq`
* Nearest Ambulance Selection
* Routing API Integration
* Dynamic Ambulance Availability
* Ambulance Status Update

## Technologies Used

* Python
* Object-Oriented Programming
* `heapq`
* `requests`
* OpenRouteService Routing API
* `python-dotenv`