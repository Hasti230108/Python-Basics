# Day 59 — Emergency Response System 

## Overview

On Day 59, I started building a **Emergency Response System** using Python OOP.

The system manages multiple ambulances and multiple emergency reports using classes, objects, lists, and methods.

This day focused mainly on understanding how different classes can work together in a real-world system.

## Concepts Learned

- Classes and Objects
- `__init__()` constructor
- Instance attributes
- Instance methods
- Lists of objects
- Object creation
- Adding objects to a collection
- Looping through objects
- Composition / "has-a" relationship
- Basic OOP system design

## Classes Created

### 1. Ambulance

Stores information about an ambulance:

- Ambulance ID
- Driver Name
- Current Location
- Status

It also contains a method to display ambulance information.

### 2. Emergency

Stores information about an emergency:

- Emergency ID
- Type of Emergency
- Urgency Level
- Emergency Location

It also contains a method to display emergency information.

### 3. EmergencySystem

Manages multiple ambulance and emergency objects.

Features implemented:

- Add ambulance
- Add emergency
- Display all ambulances
- Display all emergencies

## Sample Data

### Ambulances

* Arjun Mehta — Dadar — Available
* Sameer Khan — Bandra — Available
* Rohan Desai — Andheri — Busy

### Emergencies

* Road Accident — Kurla — High
* Chest Pain — Powai — Critical
* Fire Injury — Sion — Medium
* Breathing Problem — Worli — High

## OOP Relationship

The `EmergencySystem` has multiple `Ambulance` and `Emergency` objects.

```text
EmergencySystem
│
├── Ambulance objects
│   ├── Ambulance 101
│   ├── Ambulance 102
│   └── Ambulance 103
│
└── Emergency objects
    ├── Emergency 201
    ├── Emergency 202
    ├── Emergency 203
    └── Emergency 204
```

This demonstrates a **has-a relationship** rather than inheritance.