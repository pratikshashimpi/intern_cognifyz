import pandas as pd
from pathlib import Path


# ==========================================
# 1. LOAD DATA
# ==========================================

df = pd.read_csv("outputs/cleaned_railway_data.csv")


# ==========================================
# 2. BASIC DATASET INFORMATION
# ==========================================

total_trains = len(df)

unique_sources = df["Source_Station_Name"].nunique()

unique_destinations = df["Destination_Station_Name"].nunique()


# ==========================================
# 3. DAY-WISE ANALYSIS
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

day_counts = (
    weekly_data["days"]
    .value_counts()
    .reindex(weekdays)
)

most_common_day = day_counts.idxmax()
most_common_day_count = day_counts.max()

least_common_day = day_counts.idxmin()
least_common_day_count = day_counts.min()


# ==========================================
# 4. TOP SOURCE STATIONS
# ==========================================

top_sources = (
    weekly_data["Source_Station_Name"]
    .value_counts()
    .head(10)
)


# ==========================================
# 5. TOP DESTINATION STATIONS
# ==========================================

top_destinations = (
    weekly_data["Destination_Station_Name"]
    .value_counts()
    .head(10)
)


# ==========================================
# 6. DAY CATEGORY
# ==========================================

weekdays_only = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
]

weekends_only = [
    "Saturday",
    "Sunday"
]

weekday_count = df[df["days"].isin(weekdays_only)].shape[0]

weekend_count = df[df["days"].isin(weekends_only)].shape[0]

other_count = df.shape[0] - weekday_count - weekend_count


# ==========================================
# 7. CORRELATION
# ==========================================

day_numbers = pd.Series(
    range(1, 8),
    index=weekdays
)

correlation = day_numbers.corr(day_counts)


# ==========================================
# 8. CREATE REPORT
# ==========================================

report = f"""
# Railway Data Engineering Internship Report

## 1. Project Overview

This project analyzes railway train information using Python and Pandas.
The analysis covers data exploration, cleaning, filtering, aggregation,
data enrichment, pattern analysis, correlation analysis, visualization,
and reporting.

---

## 2. Dataset Overview

Total number of train records: **{total_trains:,}**

Unique source stations: **{unique_sources:,}**

Unique destination stations: **{unique_destinations:,}**

The dataset contains information about train numbers, train names,
source stations, destination stations, and operating days.

---

## 3. Data Cleaning

The dataset was checked for missing values.

Missing values were handled by replacing missing text values with
"UNKNOWN".

Source and destination station names were standardized by:

- Removing leading and trailing spaces.
- Converting station names to uppercase.

The cleaned dataset was saved as:

`outputs/cleaned_railway_data.csv`

---

## 4. Data Filtering

The dataset was filtered to identify trains operating on specific days.

For example:

- Saturday trains: **1,441**
- Trains starting from CST-MUMBAI: **513**

The filtered datasets were saved in the outputs folder.

---

## 5. Grouping and Aggregation

Train records were grouped according to source station.

The analysis identified stations with high numbers of originating trains.

The top source stations in the normal seven-day analysis were:

"""

for station, count in top_sources.items():
    report += f"- **{station}**: {count} trains\n"


report += f"""

---

## 6. Destination Station Analysis

The top destination stations were:

"""

for station, count in top_destinations.items():
    report += f"- **{station}**: {count} trains\n"


report += f"""

---

## 7. Day-Wise Train Distribution

The distribution of trains across the seven normal days was:

"""

for day, count in day_counts.items():
    report += f"- **{day}**: {count} trains\n"


report += f"""

### Highest Train Count

The highest number of trains was recorded on:

**{most_common_day} — {most_common_day_count} trains**

### Lowest Train Count

The lowest number of trains was recorded on:

**{least_common_day} — {least_common_day_count} trains**

The difference between the highest and lowest day was:

**{most_common_day_count - least_common_day_count} trains**

---

## 8. Weekday and Weekend Classification

The enriched dataset classified operating days into:

- Weekday
- Weekend
- Other

Results:

- Weekday records: **{weekday_count:,}**
- Weekend records: **{weekend_count:,}**
- Other records: **{other_count:,}**

The "Other" category contains the additional day values ending
with the letter "d" present in the original dataset.

These values were kept separate rather than being automatically
reclassified.

---

## 9. Correlation Analysis

A correlation value of:

**{correlation:.3f}**

was calculated by assigning numerical positions to the seven days:

Monday = 1, Tuesday = 2, ..., Sunday = 7.

The result shows the association between the imposed weekday order
and the number of train records.

Because days of the week are categorical values, this correlation
should not be interpreted as proof that the day order causes the
number of trains to increase or decrease.

---

## 10. Visualizations

The following visualizations were created:

1. `visual_bar_trains_by_day.png`
2. `visual_line_trains_by_day.png`
3. `visual_station_day_heatmap.png`
4. `visual_top_source_stations.png`
5. `visual_top_destination_stations.png`
6. `train_distribution_by_day.png`
7. `top_source_stations.png`
8. `top_destination_stations.png`
9. `day_wise_train_correlation.png`

These visualizations show train distribution by day, station-level
patterns, and station/day relationships.

---

## 11. Key Insights

### Insight 1: Train Distribution

The number of train records varies across the seven normal days.
Friday has the highest count, while Monday has the lowest count.

### Insight 2: Important Source Stations

CST-MUMBAI, SEALDAH, HOWRAH JN., KALYAN JN., and CHENNAI BEACH
are among the major source stations in the dataset.

### Insight 3: Important Destination Stations

CST-MUMBAI, SEALDAH, HOWRAH JN., KALYAN JN., and CHENNAI BEACH
are also among the major destination stations.

### Insight 4: Station-Day Distribution

The heatmap provides a visual comparison of train activity
across major source stations and different days.

### Insight 5: Data Quality

The original dataset contained no missing values in the five
main columns, but cleaning operations were still applied to
standardize the station names and provide handling for possible
missing text values.

---

## 12. Recommendations

Based on the analysis:

- Railway planners can examine high-volume source stations
  for operational planning.
- Day-wise train distributions can be used for scheduling
  analysis.
- Station/day heatmaps can help identify variations in train
  activity.
- Further analysis could include train frequency by route,
  journey duration, and seasonal patterns if those fields are
  available in a larger dataset.

---

## 13. Conclusion

The railway dataset was successfully explored, cleaned,
transformed, analyzed, and visualized using Python.

The project demonstrates the use of:

- Pandas
- Matplotlib
- Seaborn
- Data filtering
- Grouping and aggregation
- Data enrichment
- Statistical analysis
- Data visualization

The generated outputs provide a structured view of railway
train distribution by stations and operating days.

---

## 14. Output Files

Important output files are stored in the `outputs` folder:

- `cleaned_railway_data.csv`
- `saturday_trains.csv`
- `cst_mumbai_trains.csv`
- `trains_by_source_station.csv`
- `average_trains_per_day.csv`
- `enriched_railway_data.csv`
- `train_distribution_by_day.csv`
- `day_wise_train_insights.csv`
- `visual_day_counts.csv`
- `station_day_distribution.csv`

Generated charts are also stored in the `outputs` folder.
"""


# ==========================================
# 15. SAVE REPORT
# ==========================================

output_file = Path("outputs/final_railway_report.md")

output_file.write_text(
    report,
    encoding="utf-8"
)


# ==========================================
# 16. COMPLETION MESSAGE
# ==========================================

print("\n==========================================")
print("TASK 4.2 COMPLETED SUCCESSFULLY")
print("==========================================")

print("\nReport created at:")
print("outputs/final_railway_report.md")

print("\nTotal train records:", total_trains)
print("Unique source stations:", unique_sources)
print("Unique destination stations:", unique_destinations)

print("\nHighest train day:")
print(most_common_day, "-", most_common_day_count)

print("\nLowest train day:")
print(least_common_day, "-", least_common_day_count)

print("\nCorrelation:")
print(round(correlation, 3))

print("\n==========================================")
print("ALL INTERNSHIP TASKS COMPLETED")
print("==========================================")