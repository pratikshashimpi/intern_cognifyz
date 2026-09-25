import pandas as pd

# Load the cleaned railway dataset
df = pd.read_csv("outputs/cleaned_railway_data.csv")


# ==========================================
# 1. FILTER TRAINS OPERATING ON SATURDAY
# ==========================================

saturday_trains = df[
    df["days"].str.strip().str.lower() == "saturday"
]

print("\n===== TRAINS OPERATING ON SATURDAY =====")
print(saturday_trains)

print("\nNumber of Saturday trains:", len(saturday_trains))


# ==========================================
# 2. TRAINS STARTING FROM A SPECIFIC STATION
# ==========================================

# We will use CST-MUMBAI as the example station
specific_station = "CST-MUMBAI"

station_trains = df[
    df["Source_Station_Name"] == specific_station
]

print("\n===== TRAINS STARTING FROM CST-MUMBAI =====")
print(station_trains)

print("\nNumber of trains starting from CST-MUMBAI:",
      len(station_trains))


# ==========================================
# 3. SAVE FILTERED DATA
# ==========================================

saturday_trains.to_csv(
    "outputs/saturday_trains.csv",
    index=False
)

station_trains.to_csv(
    "outputs/cst_mumbai_trains.csv",
    index=False
)

print("\n===== TASK 2.1 COMPLETED =====")
print("Saturday trains saved to outputs/saturday_trains.csv")
print("CST-MUMBAI trains saved to outputs/cst_mumbai_trains.csv")