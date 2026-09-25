import pandas as pd

# Load the railway dataset
df = pd.read_csv("Railway_info.csv")

# ==========================================
# 1. NUMBER OF TRAINS
# ==========================================

number_of_trains = df["Train_No"].nunique()

print("\n===== NUMBER OF TRAINS =====")
print(number_of_trains)


# ==========================================
# 2. UNIQUE SOURCE STATIONS
# ==========================================

unique_source_stations = df["Source_Station_Name"].nunique()

print("\n===== UNIQUE SOURCE STATIONS =====")
print(unique_source_stations)


# ==========================================
# 3. UNIQUE DESTINATION STATIONS
# ==========================================

unique_destination_stations = df["Destination_Station_Name"].nunique()

print("\n===== UNIQUE DESTINATION STATIONS =====")
print(unique_destination_stations)


# ==========================================
# 4. MOST COMMON SOURCE STATIONS
# ==========================================

most_common_source = df["Source_Station_Name"].value_counts().head(10)

print("\n===== TOP 10 MOST COMMON SOURCE STATIONS =====")
print(most_common_source)


# ==========================================
# 5. MOST COMMON DESTINATION STATIONS
# ==========================================

most_common_destination = (
    df["Destination_Station_Name"]
    .value_counts()
    .head(10)
)

print("\n===== TOP 10 MOST COMMON DESTINATION STATIONS =====")
print(most_common_destination)