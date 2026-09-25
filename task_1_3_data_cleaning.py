import pandas as pd

# Load the railway dataset
df = pd.read_csv("Railway_info.csv")

# ==========================================
# 1. CHECK MISSING VALUES
# ==========================================

print("\n===== MISSING VALUES BEFORE CLEANING =====")
print(df.isnull().sum())


# ==========================================
# 2. HANDLE MISSING VALUES
# ==========================================

# Fill missing station names with "UNKNOWN"
df["Source_Station_Name"] = df["Source_Station_Name"].fillna("UNKNOWN")
df["Destination_Station_Name"] = df["Destination_Station_Name"].fillna("UNKNOWN")

# Fill missing train names
df["Train_Name"] = df["Train_Name"].fillna("UNKNOWN")

# Fill missing operating days
df["days"] = df["days"].fillna("UNKNOWN")


# ==========================================
# 3. STANDARDIZE STATION NAMES
# ==========================================

df["Source_Station_Name"] = (
    df["Source_Station_Name"]
    .str.strip()
    .str.upper()
)

df["Destination_Station_Name"] = (
    df["Destination_Station_Name"]
    .str.strip()
    .str.upper()
)


# ==========================================
# 4. CHECK MISSING VALUES AFTER CLEANING
# ==========================================

print("\n===== MISSING VALUES AFTER CLEANING =====")
print(df.isnull().sum())


# ==========================================
# 5. DISPLAY CLEANED DATA
# ==========================================

print("\n===== FIRST 10 ROWS AFTER CLEANING =====")
print(df.head(10))


# ==========================================
# 6. SAVE CLEANED DATASET
# ==========================================

df.to_csv("outputs/cleaned_railway_data.csv", index=False)

print("\n===== CLEANING COMPLETED =====")
print("Cleaned dataset saved as:")
print("outputs/cleaned_railway_data.csv")