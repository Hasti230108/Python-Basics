import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import date

# Save the records beside this Python file
DATA_FILE = Path(__file__).parent / "productivity_log.csv"

COLUMNS = [
    "Date",
    "Subject",
    "Study Hours",
    "Coding Hours",
    "Tasks Completed",
    "Mood"
]

st.set_page_config(
    page_title="My Productivity Tracker",
    page_icon="📈",
    layout="wide"
)

st.title("📈 My Personal Productivity Tracker")
st.write("Track your study sessions, coding practice, and daily progress!")

# Load existing records
if DATA_FILE.exists():
    df = pd.read_csv(DATA_FILE)
else:
    df = pd.DataFrame(columns=COLUMNS)

# Daily entry form
st.subheader("📝 Add Today's Progress")

with st.form("daily_log"):
    log_date = st.date_input("Date", value=date.today())

    subject = st.selectbox(
        "Subject studied",
        ["Python", "DBMS", "DSA", "Git & GitHub", "Other"]
    )

    col1, col2 = st.columns(2)

    with col1:
        study_hours = st.number_input(
            "Study hours",
            min_value=0.0,
            max_value=24.0,
            value=1.0,
            step=0.5
        )

    with col2:
        coding_hours = st.number_input(
            "Coding practice hours",
            min_value=0.0,
            max_value=24.0,
            value=1.0,
            step=0.5
        )

    tasks = st.text_input(
        "What did you complete?",
        placeholder="Example: Practiced Pandas groupby"
    )

    mood = st.slider(
        "How was your day? (1–10)",
        min_value=1,
        max_value=10,
        value=7
    )

    submitted = st.form_submit_button("Save Daily Log")

if submitted:
    new_entry = pd.DataFrame([{
        "Date": log_date.isoformat(),
        "Subject": subject,
        "Study Hours": study_hours,
        "Coding Hours": coding_hours,
        "Tasks Completed": tasks,
        "Mood": mood
    }])

    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)

    st.success("Daily progress saved successfully! 🎉")

# Load the latest records for analysis
if DATA_FILE.exists():
    df = pd.read_csv(DATA_FILE)

if df.empty:
    st.info("Your dashboard is waiting for your first daily log.")
else:
    # Convert columns to numeric values
    df["Study Hours"] = pd.to_numeric(df["Study Hours"])
    df["Coding Hours"] = pd.to_numeric(df["Coding Hours"])
    df["Mood"] = pd.to_numeric(df["Mood"])

    # Summary metrics
    total_study = df["Study Hours"].sum()
    total_coding = df["Coding Hours"].sum()
    total_logs = len(df)
    average_mood = df["Mood"].mean()

    st.divider()
    st.subheader("📊 Your Progress")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Study Hours", f"{total_study:.1f}")
    col2.metric("Coding Hours", f"{total_coding:.1f}")
    col3.metric("Daily Logs", total_logs)
    col4.metric("Average Mood", f"{average_mood:.1f}/10")

    # Daily progress chart
    st.subheader("📅 Daily Study vs Coding")

    daily_progress = df.groupby("Date")[
        ["Study Hours", "Coding Hours"]
    ].sum()

    st.bar_chart(daily_progress)

    # Subject-wise analysis
    st.subheader("📚 Subject-wise Study Time")

    subject_progress = df.groupby("Subject")[
        "Study Hours"
    ].sum()

    st.bar_chart(subject_progress)

    # Show complete history
    st.subheader("📋 Your Daily Logs")
    st.dataframe(df, use_container_width=True)

    # Download records
    csv_data = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇️ Download My Productivity Data",
        data=csv_data,
        file_name="my_productivity_log.csv",
        mime="text/csv"
    )

    st.caption(
        "Your dashboard uses the records saved in your local CSV file."
    )
