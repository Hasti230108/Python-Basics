import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Student Life Dashboard",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Student Life Dashboard")
st.write("Explore your weekly routine and activity patterns!")

# Sample dataset
data = {
    "Day": [
        "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"
    ],
    "Study": [3, 4, 2, 5, 4, 6, 3],
    "Sleep": [7, 8, 6, 7, 7, 9, 8],
    "Screen Time": [5, 4, 7, 3, 5, 4, 6],
    "Exercise": [1, 1, 0.5, 1, 0.5, 2, 1]
}

df = pd.DataFrame(data)

# Sidebar controls
st.sidebar.header("Dashboard Controls")

selected_days = st.sidebar.multiselect(
    "Select days",
    df["Day"].tolist(),
    default=df["Day"].tolist()
)

study_goal = st.sidebar.slider(
    "Daily study goal (hours)",
    min_value=1,
    max_value=12,
    value=4
)

# Filter dataset
filtered_df = df[df["Day"].isin(selected_days)]

if filtered_df.empty:
    st.warning("Please select at least one day.")
    st.stop()

# Summary statistics
total_study = np.sum(filtered_df["Study"])
average_sleep = np.mean(filtered_df["Sleep"])
average_screen = np.mean(filtered_df["Screen Time"])

col1, col2, col3 = st.columns(3)

col1.metric("Total Study Hours", f"{total_study:.1f}")
col2.metric("Average Sleep", f"{average_sleep:.1f} hrs")
col3.metric("Average Screen Time", f"{average_screen:.1f} hrs")

# Display data
st.subheader("📋 Weekly Routine")
st.dataframe(filtered_df, use_container_width=True)

# Study goal analysis
st.subheader("🎯 Study Goal Tracker")

goal_df = filtered_df[["Day", "Study"]].copy()
goal_df["Goal Status"] = np.where(
    goal_df["Study"] >= study_goal,
    "Goal Reached",
    "Goal Not Reached"
)

st.dataframe(goal_df, use_container_width=True)

# Study vs screen time chart
st.subheader("📊 Study vs Screen Time")

chart_df = filtered_df.set_index("Day")[["Study", "Screen Time"]]
st.bar_chart(chart_df)

# Activity comparison
st.subheader("⏱️ Total Time by Activity")

activity_totals = filtered_df[
    ["Study", "Sleep", "Screen Time", "Exercise"]
].sum()

st.bar_chart(activity_totals)

# Automatic insights
st.subheader("💡 Weekly Insights")

best_day = filtered_df.loc[
    filtered_df["Study"].idxmax(), "Day"
]

st.write(f"📚 Highest study hours: **{best_day}**")
st.write(f"🎯 Daily study goal: **{study_goal} hours**")

goals_reached = (filtered_df["Study"] >= study_goal).sum()

st.write(
    f"✅ Goal reached on {goals_reached} "
    f"out of {len(filtered_df)} selected days."
)

st.caption("Practice project using fictional student data.")