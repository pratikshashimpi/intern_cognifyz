import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned railway dataset
df = pd.read_csv("outputs/cleaned_railway_data.csv")


# ==========================================
# 1. DEFINE THE 7 DAYS OF THE WEEK
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


# ==========================================
# 2. FILTER ONLY THE 7 ACTUAL WEEKDAYS
# ==========================================

weekly_data = df[df["days"].isin(weekdays)].copy()


# ==========================================
# 3. COUNT TRAINS FOR EACH DAY
# ==========================================

day_counts = (
    weekly_data["days"]
    .value_counts()
    .reindex(weekdays)
)

print("\n===== TRAIN JOURNEYS BY DAY =====")
print(day_counts)


# ==========================================
# 4. DISPLAY DAY WITH MOST AND LEAST TRAINS
# ==========================================

most_trains_day = day_counts.idxmax()
least_trains_day = day_counts.idxmin()

print("\n===== PATTERN ANALYSIS =====")
print("Day with most trains:", most_trains_day)
print("Number of trains:", day_counts.max())

print("\nDay with least trains:", least_trains_day)
print("Number of trains:", day_counts.min())


# ==========================================
# 5. BAR PLOT - TRAINS BY DAY
# ==========================================

plt.figure(figsize=(10, 6))

day_counts.plot(kind="bar")

plt.title("Distribution of Train Journeys Throughout the Week")
plt.xlabel("Day of the Week")
plt.ylabel("Number of Trains")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("outputs/train_distribution_by_day.png")

plt.show()


# ==========================================
# 6. TOP SOURCE STATIONS
# ==========================================

source_counts = (
    weekly_data["Source_Station_Name"]
    .value_counts()
    .head(10)
)

print("\n===== TOP 10 SOURCE STATIONS =====")
print(source_counts)


# ==========================================
# 7. TOP DESTINATION STATIONS
# ==========================================

destination_counts = (
    weekly_data["Destination_Station_Name"]
    .value_counts()
    .head(10)
)

print("\n===== TOP 10 DESTINATION STATIONS =====")
print(destination_counts)


# ==========================================
# 8. BAR PLOT - TOP SOURCE STATIONS
# ==========================================

plt.figure(figsize=(12, 6))

source_counts.plot(kind="bar")

plt.title("Top 10 Source Stations")
plt.xlabel("Source Station")
plt.ylabel("Number of Trains")
plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig("outputs/top_source_stations.png")

plt.show()


# ==========================================
# 9. BAR PLOT - TOP DESTINATION STATIONS
# ==========================================

plt.figure(figsize=(12, 6))

destination_counts.plot(kind="bar")

plt.title("Top 10 Destination Stations")
plt.xlabel("Destination Station")
plt.ylabel("Number of Trains")
plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig("outputs/top_destination_stations.png")

plt.show()


# ==========================================
# 10. SAVE DAY DISTRIBUTION
# ==========================================

day_counts.to_csv(
    "outputs/train_distribution_by_day.csv",
    header=["Train_Count"]
)


# ==========================================
# 11. COMPLETION MESSAGE
# ==========================================

print("\n===== TASK 3.1 COMPLETED =====")
print("Charts saved in the outputs folder.")
print("Train distribution saved to:")
print("outputs/train_distribution_by_day.csv")