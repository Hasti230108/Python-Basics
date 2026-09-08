import pandas as pd
import numpy as np

#creating a dataframe
df = pd.DataFrame({
    'Name': ['Hasti', 'Tinker', 'Himanshi', 'Rahul', 'Rashi', 'Amisha', 'Elia', 'Tejal'],
    'Age': [18, 21, 20, 21, 19, 18, 19, 21],
    'City': ['Mumbai', 'Dadar', 'Dadar', 'Mumbai', 'Dadar', 'Mumbai', 'Dadar', 'Mumbai']
})

print("Original DataFrame:")
print(df)

#filtering
print("\nPeople older than 19:")
print(df[df['Age'] > 19])

print("\nPeople from Dadar:")
print(df[df['City'] == 'Dadar'])

#indexing
print("\nName and Age:")
print(df[['Name', 'Age']])

print("\nFirst 3 rows:")
print(df.head(3))

print("\nLast 3 rows:")
print(df.tail(3))

#missing data
df_missing = df.copy()
df_missing.loc[2, 'Age'] = np.nan
df_missing.loc[4, 'City'] = np.nan

print("\nDataframe with Missing Values:")
print(df_missing)

print("\nMissing values:")
print(df_missing.isnull().sum())

print("\nAfter dropping missing values:")
print(df_missing.dropna())

print("\nAfter filling missing values:")
print(df_missing.fillna(0))

#combining dataframes
df1 = df.iloc[:4]
df2 = df.iloc[4:]

print("\nCombined dataframe:")
print(pd.concat([df1, df2], ignore_index=True))

#grouping and aggregation
print("\nAverage age by city:")
print(df.groupby('City')['Age'].mean())

print("\nTotal age by city:")
print(df.groupby('City')['Age'].sum())

print("\nNumber of people by city:")
print(df.groupby('City').size())

#sorting
print("\nPeople sorted by age:")
print(df.sort_values('Age'))

print("\nPeople sorted by age descending:")
print(df.sort_values('Age', ascending=False))

#ranking
print("\nAge ranking:")
print(df['Age'].rank())

#top-n analysis
print("\nTop 3 oldest:")
print(df.nlargest(3, 'Age'))

print("\nTop 3 youngest:")
print(df.nsmallest(3, 'Age'))