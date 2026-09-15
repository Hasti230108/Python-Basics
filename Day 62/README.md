# Day 62 — Nearest Ambulance Selection

Today I continued building my **Emergency Response System** using Python and OOP.

The main focus was implementing **nearest ambulance selection** based on the ambulance's current location and the emergency location.

Instead of assigning the first available ambulance, the system now checks the available ambulances and selects the one with the **shortest distance** to the emergency location.

## Topics Covered

* Object-Oriented Programming
* Classes and Objects
* Composition
* Lists of Objects
* Dictionaries
* Dictionary `.get()`
* Loops and Conditions
* Searching for the minimum value
* Ambulance availability checking
* Nearest ambulance selection
* Combining multiple OOP methods
* Updating object status

## 1. Ambulance Selection

Previously, the system assigned the first available ambulance.

Now it checks:

```text
Available ambulances
        ↓
Check distance from emergency
        ↓
Compare distances
        ↓
Find shortest distance
        ↓
Select nearest ambulance
```

## 2. Distance Mapping

For this beginner-level version, distances between locations were stored manually using a dictionary.

Example:

```python
distances = {
    ("Dadar", "Sion"): 4,
    ("Bandra", "Sion"): 8,
    ("Andheri", "Sion"): 10
}
```

This allows the system to compare the distance of different ambulances from an emergency location.

## 3. Finding the Nearest Ambulance

The system checks only ambulances whose status is:

```text
Available
```

It then compares their distances and selects the ambulance with the shortest distance.

For example:

```text
Ambulance 101 → Dadar → Sion → 4 km
Ambulance 102 → Bandra → Sion → 8 km
Ambulance 103 → Andheri → Sion → Busy
```

Therefore:

```text
Nearest Available Ambulance → Ambulance 101
Distance → 4 km
```

## 4. Ambulance Assignment

The existing assignment functionality was also tested together with the nearest ambulance feature.

After Ambulance 101 was assigned to an emergency, its status changed from:

```text
Available
```

to:

```text
Busy
```

The system then searched again for an available ambulance.

The next nearest ambulance was:

```text
Ambulance 102
Distance → 8 km
```

## Practical Testing

### Test 1 — Find nearest ambulance

Emergency Location:

```text
Sion
```

Available ambulances:

```text
Ambulance 101 → Dadar → 4 km
Ambulance 102 → Bandra → 8 km
```

Result:

```text
Ambulance 101 selected
Distance: 4 km
```

### Test 2 — After assignment

After Ambulance 101 was assigned:

```text
Ambulance 101 → Busy
```

The system searched again.

Result:

```text
Ambulance 102 selected
Distance: 8 km
```

## Current System Structure

```text
Emergency Response System
│
├── Ambulance
│   ├── ID
│   ├── Driver Name
│   ├── Current Location
│   └── Status
│
├── Emergency
│   ├── Emergency ID
│   ├── Emergency Type
│   ├── Urgency
│   └── Location
│
└── EmergencySystem
    ├── Add Ambulance
    ├── Add Emergency
    ├── Display Ambulances
    ├── Display Emergencies
    ├── Find Highest Priority Emergency
    ├── Find Nearest Ambulance
    └── Assign Ambulance
```

## Key Learning

> The system should not simply choose the first available ambulance.

> It should compare available options and select the most suitable one.

Today I learned how to use a dictionary and loops to implement a simple **nearest-resource selection algorithm**.

This also helped me understand how multiple OOP methods can work together to create a larger system.