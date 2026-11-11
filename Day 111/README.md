# Day 111 — Export Calculation History as CSV

Today, I upgraded my Streamlit Simple Calculator by adding a feature to **download calculation history as a CSV file**.

Users can now export their previous calculations and open them in spreadsheet applications such as Microsoft Excel or Google Sheets.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Division-by-zero handling
- Calculation history using Streamlit Session State
- Clear History button
- Download calculation history as a CSV file

## Concepts Learned

- Importing Python's `csv` module
- Using `io.StringIO()` to create an in-memory text file
- Creating CSV files with `csv.DictWriter()`
- Writing column headings using `writeheader()`
- Writing multiple records using `writerows()`
- Retrieving CSV content using `getvalue()`
- Using Streamlit's `st.download_button()`
- Understanding CSV MIME types

## How CSV Export Works

1. Calculation history is stored in `st.session_state.history`.
2. `io.StringIO()` creates a temporary file in memory.
3. `csv.DictWriter()` converts the calculation dictionaries into CSV format.
4. `st.download_button()` allows users to download the generated file.

**Downloaded file:** `calculation_history.csv`

**Note:** The CSV is downloaded through the browser. Its save location depends on the browser's download settings. Calculation history is temporary and is not permanently stored by the application.

## Technologies Used

- Python
- Streamlit
- CSV
- IO

## Key Takeaways

I learned how to convert Python dictionaries into CSV records and provide downloadable files directly through a Streamlit application.

I also understood the difference between temporarily storing data in memory and downloading it as a separate file.

---

Successfully implemented CSV export functionality for the calculator's calculation history.
