import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ==========================================
# 1. LOAD DATA
# ==========================================

df = pd.read_csv("outputs/cleaned_railway_data.csv")


# ==========================================
# 2. SELECT THE 7 ACTUAL DAYS
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

weekly_data = df[df["days"].isin(weekdays)].copy()


# ==========================================
# 3. BAR CHART - TRAINS BY DAY
# ==========================================

day_counts = (
    weekly_data["days"]
    .value_counts()
    .reindex(weekdays)
)

plt.figure(figsize=(10, 6))

day_counts.plot(kind="bar")

plt.title("Number of Trains by Day")
plt.xlabel("Day")
plt.ylabel("Number of Trains")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("outputs/visual_bar_trains_by_day.png")

plt.show()


# ==========================================
# 4. LINE CHART - TRAINS BY DAY
# ==========================================

plt.figure(figsize=(10, 6))

plt.plot(
    weekdays,
    day_counts.values,
    marker="o"
)

plt.title("Train Journey Trend Throughout the Week")
plt.xlabel("Day")
plt.ylabel("Number of Trains")
plt.xticks(rotation=45)

plt.grid(True)

plt.tight_layout()

plt.savefig("outputs/visual_line_trains_by_day.png")

plt.show()


# ==========================================
# 5. SOURCE STATION COUNTS
# ==========================================

source_counts = (
    weekly_data["Source_Station_Name"]
    .value_counts()
    .head(10)
)

print("\n===== TOP 10 SOURCE STATIONS =====")
print(source_counts)


# ==========================================
# 6. DESTINATION STATION COUNTS
# ==========================================

destination_counts = (
    weekly_data["Destination_Station_Name"]
    .value_counts()
    .head(10)
)

print("\n===== TOP 10 DESTINATION STATIONS =====")
print(destination_counts)


# ==========================================
# 7. CREATE STATION-DAY DATA
# ==========================================

station_day = pd.crosstab(
    weekly_data["Source_Station_Name"],
    weekly_data["days"]
)

# Keep only the top 15 source stations
top_stations = source_counts.head(15).index

station_day_top = station_day.reindex(
    top_stations,
    fill_value=0
)

# Arrange columns in weekday order
station_day_top = station_day_top.reindex(
    columns=weekdays,
    fill_value=0
)


# ==========================================
# 8. HEATMAP - SOURCE STATION VS DAY
# ==========================================

plt.figure(figsize=(12, 8))

sns.heatmap(
    station_day_top,
    annot=True,
    fmt="d",
    cmap="YlGnBu"
)

plt.title("Train Distribution by Source Station and Day")
plt.xlabel("Day of the Week")
plt.ylabel("Source Station")

plt.tight_layout()

plt.savefig("outputs/visual_station_day_heatmap.png")

plt.show()


# ==========================================
# 9. BAR CHART - TOP SOURCE STATIONS
# ==========================================

plt.figure(figsize=(12, 6))

source_counts.plot(kind="bar")

plt.title("Top 10 Source Stations")
plt.xlabel("Source Station")
plt.ylabel("Number of Trains")
plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig("outputs/visual_top_source_stations.png")

plt.show()


# ==========================================
# 10. BAR CHART - TOP DESTINATION STATIONS
# ==========================================

plt.figure(figsize=(12, 6))

destination_counts.plot(kind="bar")

plt.title("Top 10 Destination Stations")
plt.xlabel("Destination Station")
plt.ylabel("Number of Trains")
plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig("outputs/visual_top_destination_stations.png")

plt.show()


# ==========================================
# 11. SAVE VISUALIZATION DATA
# ==========================================

day_counts.to_csv(
    "outputs/visual_day_counts.csv",
    header=["Train_Count"]
)

station_day_top.to_csv(
    "outputs/station_day_distribution.csv"
)


# ==========================================
# 12. COMPLETION MESSAGE
# ==========================================

print("\n===== TASK 4.1 COMPLETED =====")

print("Bar chart saved:")
print("outputs/visual_bar_trains_by_day.png")

print("\nLine chart saved:")
print("outputs/visual_line_trains_by_day.png")

print("\nHeatmap saved:")
print("outputs/visual_station_day_heatmap.png")

print("\nSource station chart saved:")
print("outputs/visual_top_source_stations.png")

print("\nDestination station chart saved:")
print("outputs/visual_top_destination_stations.png")