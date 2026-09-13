# Day 60 — Emergency Response Logic 

## Overview

Day 60 continued the **Emergency Response System** project created on Day 59.

The focus of this day was to add decision-making logic to the system. The program can now search for a particular emergency, find an available ambulance, assign it to the emergency, and update the ambulance's status.

## Objectives

* Add ambulance assignment functionality.
* Search for emergencies using Emergency ID.
* Find an available ambulance.
* Change ambulance status from `Available` to `Busy`.
* Handle invalid Emergency IDs.
* Handle situations where no ambulance is available.
* Practice loops, conditions, flags, and `return`.

## Concepts Practiced

* Object-Oriented Programming
* Classes and Objects
* Composition
* Lists of Objects
* `for` loops
* `if` conditions
* Boolean flags
* Searching objects by ID
* State modification
* Basic error handling
* Real-world decision logic

## New Functionality

Added the `assign_ambulance()` method to the `EmergencySystem` class.

The method:

1. Searches for the given Emergency ID.
2. Confirms whether the emergency exists.
3. Searches through the ambulance list.
4. Finds the first ambulance with `Available` status.
5. Assigns the ambulance to the emergency.
6. Changes its status to `Busy`.
7. Displays assignment details.
8. Shows an appropriate message if the emergency doesn't exist or no ambulance is available.

## Testing

The system was tested with:

### Valid Emergency

Emergency `203` was successfully assigned to Ambulance `101`.

### Invalid Emergency

Emergency `205` was tested and correctly displayed:

```text
Emergency ID 205 not found!
```

### Multiple Assignments

Emergency `202` was successfully assigned to Ambulance `102`.

### No Available Ambulance

After Ambulances `101` and `102` became busy, another assignment correctly displayed:

```text
No available ambulance!
```