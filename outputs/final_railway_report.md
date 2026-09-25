
# Railway Data Engineering Internship Report

## 1. Project Overview

This project analyzes railway train information using Python and Pandas.
The analysis covers data exploration, cleaning, filtering, aggregation,
data enrichment, pattern analysis, correlation analysis, visualization,
and reporting.

---

## 2. Dataset Overview

Total number of train records: **11,113**

Unique source stations: **921**

Unique destination stations: **924**

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

- **CST-MUMBAI**: 510 trains
- **SEALDAH**: 367 trains
- **HOWRAH JN.**: 332 trains
- **KALYAN JN**: 285 trains
- **CHENNAI BEACH**: 222 trains
- **THANE**: 186 trains
- **PANVEL**: 140 trains
- **TAMBARAM**: 140 trains
- **NEW DELHI**: 107 trains
- **RAVLI JN**: 99 trains


---

## 6. Destination Station Analysis

The top destination stations were:

- **CST-MUMBAI**: 511 trains
- **SEALDAH**: 368 trains
- **HOWRAH JN.**: 331 trains
- **KALYAN JN**: 284 trains
- **CHENNAI BEACH**: 222 trains
- **THANE**: 194 trains
- **PANVEL**: 143 trains
- **TAMBARAM**: 140 trains
- **NEW DELHI**: 107 trains
- **RAVLI JN**: 93 trains


---

## 7. Day-Wise Train Distribution

The distribution of trains across the seven normal days was:

- **Monday**: 1342 trains
- **Tuesday**: 1454 trains
- **Wednesday**: 1448 trains
- **Thursday**: 1372 trains
- **Friday**: 1471 trains
- **Saturday**: 1441 trains
- **Sunday**: 1432 trains


### Highest Train Count

The highest number of trains was recorded on:

**Friday — 1471 trains**

### Lowest Train Count

The lowest number of trains was recorded on:

**Monday — 1342 trains**

The difference between the highest and lowest day was:

**129 trains**

---

## 8. Weekday and Weekend Classification

The enriched dataset classified operating days into:

- Weekday
- Weekend
- Other

Results:

- Weekday records: **7,087**
- Weekend records: **2,873**
- Other records: **1,153**

The "Other" category contains the additional day values ending
with the letter "d" present in the original dataset.

These values were kept separate rather than being automatically
reclassified.

---

## 9. Correlation Analysis

A correlation value of:

**0.435**

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
