# Day 103 — SpamShield: SMS Spam Dataset Exploration

Today, I started building **SpamShield**, a machine learning project that aims to classify SMS messages as spam or legitimate (ham).

I loaded the SMS Spam Collection dataset using Pandas and explored its structure, label distribution, missing values, and duplicate messages before training a model.

## Objectives

- Load a real-world SMS dataset.
- Understand the dataset's rows and columns.
- Count spam and legitimate messages.
- Calculate label percentages.
- Check for missing values.
- Identify duplicate rows.
- Check whether identical messages have conflicting labels.

## Technologies Used

- Python
- Pandas
- `pathlib`

## Project Structure

```text
Day 103/
├── data/
│   └── SMSSpamCollection
├── explore_dataset.py
└── README.md
```

The dataset file is stored in the `data` folder. Python's `pathlib` is used to locate the file relative to the script, making the file path more reliable.

## Dataset Overview

The project uses the SMS Spam Collection dataset, a public collection of labelled SMS messages. <https://archive.ics.uci.edu/dataset/228/sms+spam+collection>

| Property | Result |
|---|---:|
| Total messages | 5,572 |
| Total columns | 2 |
| Legitimate messages (ham) | 4,825 |
| Spam messages | 747 |
| Missing values | 0 |
| Duplicate rows | 403 |
| Messages with conflicting labels | 0 |

### Dataset Columns

- `label` — identifies a message as `ham` or `spam`.
- `message` — contains the actual SMS text.

## Label Distribution

| Label | Count | Percentage |
|---|---:|---:|
| Ham | 4,825 | 86.59% |
| Spam | 747 | 13.41% |
| **Total** | **5,572** | **100%** |

The dataset contains considerably more legitimate messages than spam messages. This is an example of **class imbalance**, which we will need to consider when evaluating our future machine learning model.

## Data Quality Checks

### 1. Missing Values

Used `df.isnull().sum()` to check for missing values.

**Result:** No missing values were found in either column.

### 2. Duplicate Rows

Used `df.duplicated().sum()` to count repeated rows.

**Result:** 403 duplicate rows were detected.

### 3. Conflicting Labels

Grouped messages by their text and checked how many different labels each identical message had.

**Result:** Zero messages had conflicting labels.

This means no identical message text was found with both `ham` and `spam` labels in this dataset.

Duplicates will be handled carefully before model evaluation to reduce the risk of similar or identical messages appearing in both training and testing data.

## Concepts Practiced

- Loading tab-separated data with `pd.read_csv()`.
- Using `Path(__file__).resolve().parent` to build reliable file paths.
- Exploring data with `head()` and `shape`.
- Counting categories with `value_counts()`.
- Calculating percentages with `normalize=True`.
- Checking missing values with `isnull().sum()`.
- Detecting duplicates with `duplicated()`.
- Grouping messages to check label consistency.

## Key Takeaways

- Data exploration is an important first step in machine learning.
- Text datasets need preparation before they can be used by most traditional ML algorithms.
- Class imbalance can make accuracy alone misleading.
- Duplicate records should be investigated before splitting data for training and testing.
- Checking label consistency helps identify potential data-quality issues.