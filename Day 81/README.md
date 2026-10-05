# Day 81 — Matplotlib Data Visualization

Today I learned and practiced **Matplotlib** in Python for creating visual representations of data.

I used student marks data and created different types of charts to understand how the same dataset can be visualized in different ways.

## Topics Covered

- Introduction to Matplotlib
- Importing `matplotlib.pyplot`
- Bar Charts
- Line Charts
- Pie Charts
- Scatter Plots
- Chart Titles
- X-axis and Y-axis Labels
- Markers
- Pie Chart Percentages

## 1. Bar Chart

Used `plt.bar()` to compare the marks of different students.

```python
plt.bar(students, marks)
```

## 2. Line Chart

Used `plt.plot()` to visualize the marks as a line and added markers using `marker="o"`.

```python
plt.plot(students, marks, marker="o")
```

## 3. Pie Chart

Used `plt.pie()` to represent the marks as parts of a whole.

```python
plt.pie(marks, labels=students, autopct="%1.1f%%")
```

## 4. Scatter Plot

Used `plt.scatter()` to create a scatter visualization of the student marks.

```python
plt.scatter(students, marks)
```

## Key Takeaways

> Matplotlib is used to visualize and understand data through graphs and charts.

> Different charts are useful for different types of data analysis.

> `bar()` → Bar Chart
> `plot()` → Line Chart
> `pie()` → Pie Chart
> `scatter()` → Scatter Plot

## Library Used

**Matplotlib**

```python
import matplotlib.pyplot as plt
```