# Day 61 — Emergency Response System: Priority Logic 

## Overview

Day 61 improved the **Emergency Response System** by introducing emergency priority levels.

The system can now determine which emergency has the highest priority based on its urgency level.

## Objectives

* Add emergency priority levels.
* Assign numerical values to different urgency levels.
* Find the highest-priority emergency.
* Continue using the ambulance assignment system from Day 60.
* Handle different emergency scenarios.

## Concepts Practiced

* Object-Oriented Programming
* Classes and Objects
* Composition
* Dictionaries
* `for` loops
* Conditional statements
* Object comparison
* Searching through objects
* State management
* Decision-making logic

## Priority System

The following priority levels were implemented:

```text
Critical → 4
High     → 3
Medium   → 2
Low      → 1
```

A higher number represents a higher emergency priority.

## New Functionality

Added:

```python
find_highest_priority_emergency()
```

This method checks all stored emergencies and identifies the emergency with the highest urgency.

For the current test data:

```text
201 → High
202 → Critical
203 → Medium
204 → High
```

The system correctly identifies **Emergency 202 — Chest Pain** as the highest-priority emergency.

## Testing

The system was tested for:

* Ambulance assignment 
* Invalid Emergency ID 
* No available ambulance 
* Highest-priority emergency detection 

Output:

```text
===== HIGHEST PRIORITY EMERGENCY =====
Emergency ID: 202
Emergency: Chest Pain
Priority: Critical
Location: Powai
```