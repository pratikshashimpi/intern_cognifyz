import pandas as pd

# Load the cleaned railway dataset
df = pd.read_csv("outputs/cleaned_railway_data.csv")


# ==========================================
# 1. COUNT TRAINS BY SOURCE STATION
# ==========================================

trains_by_source = (
    df.groupby("Source_Station_Name")
    .size()
    .sort_values(ascending=False)
)

print("\n===== NUMBER OF TRAINS BY SOURCE STATION =====")
print(trains_by_source.head(20))


# ==========================================
# 2. KEEP THE 7 ACTUAL DAYS OF THE WEEK
# ==========================================

weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

weekday_df = df[df["days"].isin(weekdays)]


# ==========================================
# 3. AVERAGE TRAINS PER DAY FOR EACH
#    SOURCE STATION
# ==========================================

average_trains_per_day = (
    weekday_df.groupby("Source_Station_Name")
    .size()
    / 7
)

average_trains_per_day = average_trains_per_day.sort_values(
    ascending=False
)

print("\n===== AVERAGE TRAINS PER DAY BY SOURCE STATION =====")
print(average_trains_per_day.head(20))


# ==========================================
# 4. SAVE RESULTS
# ==========================================

trains_by_source.to_csv(
    "outputs/trains_by_source_station.csv",
    header=["Train_Count"]
)

average_trains_per_day.to_csv(
    "outputs/average_trains_per_day.csv",
    header=["Average_Trains_Per_Day"]
)


# ==========================================
# 5. COMPLETION MESSAGE
# ==========================================

print("\n===== TASK 2.2 COMPLETED =====")

print("Train counts saved to:")
print("outputs/trains_by_source_station.csv")

print("\nAverage trains per day saved to:")
print("outputs/average_trains_per_day.csv")