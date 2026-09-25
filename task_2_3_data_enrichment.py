import pandas as pd

# Load the cleaned railway dataset
df = pd.read_csv("outputs/cleaned_railway_data.csv")


# ==========================================
# 1. DEFINE WEEKDAYS AND WEEKENDS
# ==========================================

weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
]

weekends = [
    "Saturday",
    "Sunday"
]


# ==========================================
# 2. CREATE TRAIN CATEGORY
# ==========================================

def categorize_day(day):
    if day in weekdays:
        return "Weekday"
    elif day in weekends:
        return "Weekend"
    else:
        return "Other"


df["Day_Category"] = df["days"].apply(categorize_day)


# ==========================================
# 3. DISPLAY RESULTS
# ==========================================

print("\n===== DATA WITH DAY CATEGORY =====")
print(df.head(20))


# ==========================================
# 4. COUNT EACH CATEGORY
# ==========================================

print("\n===== DAY CATEGORY COUNTS =====")
print(df["Day_Category"].value_counts())


# ==========================================
# 5. SAVE ENRICHED DATASET
# ==========================================

df.to_csv(
    "outputs/enriched_railway_data.csv",
    index=False
)


# ==========================================
# 6. COMPLETION MESSAGE
# ==========================================

print("\n===== TASK 2.3 COMPLETED =====")
print("Enriched dataset saved to:")
print("outputs/enriched_railway_data.csv")