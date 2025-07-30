import pandas as pd

# load a csv file
df = pd.read_csv("part-02/data.csv")
print(df.head())

# shape of data frame
print(df.shape)

# data types
print(df.dtypes)

# summary statistics
print(df.describe())

# null values
print(df.isnull().sum())

# column names as a list 
print(df.columns.tolist())

# fill missing values
df['age'] = df['age'].fillna(40)

# drop rows with missing values
df = df.dropna()

# check for duplicates
print(f"duplicates: {df.duplicated().sum()}")

# remove duplicates
df = df.drop_duplicates()

# apply transformation
df['name'] = df['name'].str.upper()

# normalizer numeric data
df['age'] = (df['age'] - df['age'].mean()) / df['age'].std()

# rename columns
df = df.rename(columns={"age": "how old"})

# few rows
print(df.head())
print(df.shape)

