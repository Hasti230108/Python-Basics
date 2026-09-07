import pandas as pd
import numpy as np

#Creating a DataFrame
df = pd.DataFrame({
    'Name': ['Hasti', "Tinker", 'Himanshi', "Rahul", 'Ananya', "Elia", 'Twinkle', "Tahseen"],
    'Age': [18, 21, 20, 21, 19, 18, 19, 21],
    'City': ['Mumbai', 'Dadar', 'Dadar', 'Mumbai', 'Dadar', 'Mumbai', 'Dadar', 'Mumbai']
})

#Displaying the dataframe
print("Original DataFrame:")
print(df)

#Indexing and Filtering
print("\nFiltering rows where Age is greater than 19:")
print(df[df['Age'] > 19])
print("\nFiltering rows where City is 'Dadar':")
print(df[df['City'] == 'Dadar'])
print("\nIndexing specific columns (Name and Age):")
print(df[['Name', 'Age']])
print("\nIndexing specific rows (first 3 rows):")
print(df.head(3))
print("\nIndexing specific rows (last 3 rows):")
print(df.tail(3))

#missing ddata handling
df_with_missing = df.copy()
df_with_missing.loc[2, 'Age'] = np.nan
df_with_missing.loc[4, 'City'] = np.nan
print("\nDataFrame with missing values:")
print(df_with_missing)
print("\nHandling missing data:")
print("Number of missing values in each column:")
print(df_with_missing.isnull().sum())
print("\nDropping rows with any missing values:")
print(df_with_missing.dropna())
print("\nFilling missing values with a specific value:")
print(df_with_missing.fillna(0))

#Combining DataFrames
df1 = pd.DataFrame({
    'Name': ['Hasti', "Tinker", 'Himanshi'],
    'Age': [18, 21, 20],
    'City': ['Mumbai', 'Dadar', 'Dadar']
})
df2 = pd.DataFrame({
    'Name': ['Rahul', 'Ananya', 'Elia'],
    'Age': [21, 19, 18],
    'City': ['Mumbai', 'Dadar', 'Mumbai']
})
print("\nCombined DataFrame:")
print(pd.concat([df1, df2], ignore_index=True))

#Grouping and Aggregation
print("\nGrouping by City and calculating mean Age:")
print(df.groupby('City')['Age'].mean())
print("\nGrouping by City and calculating sum of Age:")
print(df.groupby('City')['Age'].sum())
print("\nGrouping by City and counting number of entries:")
print(df.groupby('City').size())

#rankin and top-n analysis
print("\nRanking by Age:")
print(df['Age'].rank())
print("\nTop 3 oldest individuals:")
print(df.nlargest(3, 'Age'))
print("\nTop 3 youngest individuals:")
print(df.nsmallest(3, 'Age'))