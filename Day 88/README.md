# Python Day 88 — Personal Productivity Tracker

Today I built a **Personal Productivity Tracker** using Python, Streamlit, and Pandas.

This project helps me track my daily study hours, coding practice, subjects studied, completed tasks, and mood. It transforms my daily records into useful summaries and charts so I can understand my productivity over time.

## Concepts Practiced

- Streamlit forms and interactive input widgets
- Date inputs, dropdown menus, and sliders
- Creating and updating Pandas DataFrames
- Reading and writing CSV files
- Appending records using `pd.concat()`
- Grouping data using `groupby()`
- Calculating totals and averages
- Data visualization with bar charts
- Downloading data as a CSV file
- Using `pathlib` to manage file paths
- Ignoring private data using `.gitignore`

## Features

### 1. Daily Progress Logging
Record your daily progress, including:
- Date
- Subject studied
- Study hours
- Coding practice hours
- Completed tasks
- Mood rating from 1 to 10

### 2. Productivity Summary
View important statistics:
- Total study hours
- Total coding hours
- Number of daily logs
- Average mood rating

### 3. Daily Progress Analysis
Compare study hours and coding hours across different dates using a bar chart.

### 4. Subject-wise Analysis
Analyze the total study time spent on each subject.

### 5. CSV Data Storage
Daily entries are saved in `productivity_log.csv`, allowing the application to load previous records when reopened.

### 6. Download Productivity Data
Download your saved productivity records as a CSV file for future analysis.

## Technologies Used

- **Python** — Application logic
- **Streamlit** — Interactive web interface
- **Pandas** — Data storage and analysis

## Project Structure

```text
Day 88/
├── .gitignore
├── personal_productivity_tracker.py
├── productivity_log.csv
└── README.md
```

The application automatically creates `productivity_log.csv` when the first entry is saved.

The personal CSV file is excluded from Git tracking through `.gitignore`.

## Key Learning

This project helped me understand how Python can be used to build an interactive application that stores real daily records and turns them into meaningful insights.

It combines user input, data persistence, data analysis, and visualization in one practical project.