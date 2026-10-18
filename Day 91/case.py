
case = {
    "title": "The Missing Diamond",
    "story": (
        "A diamond disappeared from a locked museum "
        "display at 8:00 PM. Three people were nearby. "
        "Your job is to investigate the clues and "
        "identify who took it."
    ),
    "suspects": [
        "Alex - The museum guard",
        "Mia - The visiting artist",
        "Noah - The museum manager"
    ],
    "clues": [
        "The display was opened with a manager's key.",
        "Alex was seen near the entrance at 7:55 PM.",
        "Mia left the museum before 8:00 PM."
    ]
}

print("=" * 40)
print("       MYSTERY 100")
print("=" * 40)

print("\nCASE:", case["title"])
print("\nSTORY:")
print(case["story"])

print("\nSUSPECTS:")
for suspect in case["suspects"]:
    print("-", suspect)

print("\nEVIDENCE:")
for number, clue in enumerate(case["clues"], start=1):
    print(f"{number}. {clue}")

print("\nYour investigation starts now!")
print("Who do you suspect, and why?")