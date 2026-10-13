import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "Study_Hours": [3, 4, 2, 5, 4, 6, 3],
    "Sleep_Hours": [7, 8, 6, 7, 7, 9, 8],
    "Screen_Time": [5, 4, 7, 3, 5, 4, 6],
    "Exercise_Hours": [1, 1, 0.5, 1, 0.5, 2, 1]
}

df = pd.DataFrame(data)

print("=" * 40)
print("          STUDENT LIFE ANALYZER")
print("=" * 40)

print("\nWEEKLY ROUTINE")
print(df.to_string(index=False))

study = df["Study_Hours"].to_numpy()
sleep = df["Sleep_Hours"].to_numpy()
screen = df["Screen_Time"].to_numpy()

print("\nWEEKLY STATISTICS")
print("Total study hours:", np.sum(study))
print("Average study hours:", round(np.mean(study), 2))
print("Average sleep hours:", round(np.mean(sleep), 2))
print("Average screen time:", round(np.mean(screen), 2))
print("Most study hours in one day:", np.max(study))
print("Least study hours in one day:", np.min(study))

best_study_day = df.loc[df["Study_Hours"].idxmax(), "Day"]
most_screen_day = df.loc[df["Screen_Time"].idxmax(), "Day"]
most_sleep_day = df.loc[df["Sleep_Hours"].idxmax(), "Day"]

print("\nAUTOMATIC INSIGHTS")
print("Highest study time:", best_study_day)
print("Highest screen time:", most_screen_day)
print("Most sleep:", most_sleep_day)

df["Study_Screen_Difference"] = (df["Study_Hours"] - df["Screen_Time"]).apply(lambda x: f"{x:+.1f} hours")

print("\nSTUDY VS SCREEN TIME")
print(df[["Day", "Study_Screen_Difference"]].to_string(index=False))

plt.figure(figsize=(9, 5))
plt.bar(df["Day"], df["Study_Hours"], label="Study Hours")
plt.plot(
    df["Day"],
    df["Screen_Time"],
    marker="o",
    label="Screen Time"
)

plt.title("Weekly Study Hours vs Screen Time")
plt.xlabel("Day")
plt.ylabel("Hours")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.4)
plt.tight_layout()
plt.show()

activity_totals = df[
    ["Study_Hours", "Sleep_Hours", "Screen_Time", "Exercise_Hours"]
].sum()

plt.figure(figsize=(8, 5))
activity_totals.plot(kind="bar")
plt.title("Total Time by Activity During the Week")
plt.xlabel("Activity")
plt.ylabel("Total Hours")
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()
