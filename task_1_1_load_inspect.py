import pandas as pd

# Load the railway dataset
df = pd.read_csv("Railway_info.csv")

# Display the first 10 rows
print("\n===== FIRST 10 ROWS =====")
print(df.head(10))

# Display dataset information
print("\n===== DATASET INFORMATION =====")
df.info()

# Display data types
print("\n===== DATA TYPES =====")
print(df.dtypes)

# Check missing values
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# Display number of rows and columns
print("\n===== DATASET SHAPE =====")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])