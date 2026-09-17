# Day 64 — Priority-Based Emergency Dispatch

Today I improved my **Emergency Response System** by implementing a **Priority Queue** using Python's `heapq` module.

The system can now process emergencies based on their urgency instead of simply processing them in the order they were added.

## Topics Covered

- Priority Queue
- Python `heapq` module
- `heappush()`
- `heappop()`
- Tuples in Priority Queues
- Priority-based processing
- OOP + DSA integration
- Dynamic ambulance availability
- Emergency dispatch workflow
- Integration with the routing API

## 1. Priority Queue

A Priority Queue processes elements based on their priority.

For the emergency system, the priority order is:

```text
Critical → High → Medium → Low
````

The priority numbers used by `heapq` are:

```text
Critical → 1
High → 2
Medium → 3
Low → 4
```

Since `heapq` removes the smallest value first, Critical emergencies are processed first.

## 2. Using `heapq`

Python's `heapq` module provides functions for implementing a priority queue.

### Adding an emergency

```python
heapq.heappush(priority_queue, emergency)
```

### Removing the highest-priority emergency

```python
heapq.heappop(priority_queue)
```

## 3. Emergency Queue Structure

Each emergency is stored as a tuple:

```python
(
    priority,
    emergency_id,
    emergency_description,
    emergency_location
)
```

Example:

```python
(1, 202, "Chest Pain", "Powai")
```

Here:

* `1` → Priority
* `202` → Emergency ID
* `"Chest Pain"` → Emergency description
* `"Powai"` → Emergency location

## 4. Priority Dispatch

The system adds all emergencies to the priority queue.

```python
system.add_to_priority_queue()
```

Then processes them:

```python
system.process_priority_queue()
```

The emergencies are processed in this order:

```text
202 → Critical
205 → Critical
201 → High
204 → High
203 → Medium
206 → Low
```

## 5. Automatic Ambulance Assignment

After selecting an emergency from the priority queue, the system automatically calls:

```python
self.assign_ambulance(emgy_id)
```

The system then:

1. Finds available ambulances
2. Calculates road distance using the routing API
3. Finds the nearest available ambulance
4. Assigns the ambulance
5. Changes its status from `Available` to `Busy`

## 6. Routing API Integration

The priority dispatch system continues using the routing API integrated on Day 63.

The API provides:

* Road distance
* Estimated travel time
* Route information

Example:

```text
Ambulance ID: 101
Current Location: Dadar
Emergency Location: Worli
Distance: 2.91 km
Estimated Time: 5.56 minutes
```

## 7. Dynamic Ambulance Availability

The system dynamically changes ambulance status after assignment.

Example:

```text
Available → Busy
```

Initially there were 4 available ambulances.

After processing four emergencies, all available ambulances became busy.

Therefore, the remaining emergencies could not be assigned:

```text
Fire Injury → No suitable ambulance
Medical Emergency → No suitable ambulance
```

This demonstrates how the system handles limited ambulance availability.

## Practical Work Completed

* Created a priority queue using `heapq`
* Used `heappush()` to add emergencies
* Used `heappop()` to process emergencies
* Stored emergency details inside tuples
* Implemented priority-based emergency processing
* Connected the priority queue with `EmergencySystem`
* Connected priority dispatch with ambulance assignment
* Used routing API to find the nearest ambulance
* Dynamically changed ambulance status
* Handled situations where no ambulance was available

## Key Takeaways

> A Priority Queue processes elements according to their priority.

> `heapq` removes the smallest-priority value first.

> `heappush()` adds an item to the priority queue.

> `heappop()` removes the highest-priority item.

> Priority Queues can be combined with OOP and DSA to build real-world systems.

> The ambulance system can now process emergencies automatically according to urgency.

## Technologies Used

* Python
* OOP
* `heapq`
* `requests`
* Python Dotenv
* OpenRouteService / HeiGIT Routing API