import pandas as pd
import matplotlib.pyplot as plt


# ==========================================
# 1. LOAD THE CLEANED DATASET
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
# 3. COUNT TRAINS FOR EACH DAY
# ==========================================

day_counts = (
    weekly_data["days"]
    .value_counts()
    .reindex(weekdays)
)

print("\n===== TRAIN COUNT BY DAY =====")
print(day_counts)


# ==========================================
# 4. CALCULATE CORRELATION
# ==========================================

# Assign a numerical order to the days
day_numbers = pd.Series(
    range(1, 8),
    index=weekdays
)

correlation = day_numbers.corr(day_counts)

print("\n===== CORRELATION ANALYSIS =====")
print("Correlation between day order and train count:")
print(round(correlation, 4))


# ==========================================
# 5. IDENTIFY HIGHEST AND LOWEST DAYS
# ==========================================

highest_day = day_counts.idxmax()
lowest_day = day_counts.idxmin()

highest_count = day_counts.max()
lowest_count = day_counts.min()

print("\n===== KEY FINDINGS =====")
print("Highest train count:", highest_day, "-", highest_count)
print("Lowest train count:", lowest_day, "-", lowest_count)


# ==========================================
# 6. CALCULATE DIFFERENCE
# ==========================================

difference = highest_count - lowest_count

print("\nDifference between highest and lowest:")
print(difference)


# ==========================================
# 7. PERCENTAGE DIFFERENCE
# ==========================================

percentage_difference = (
    difference / lowest_count
) * 100

print("\nPercentage difference:")
print(round(percentage_difference, 2), "%")


# ==========================================
# 8. CREATE INSIGHTS DATAFRAME
# ==========================================

insights = pd.DataFrame({
    "Day": weekdays,
    "Train_Count": day_counts.values
})

print("\n===== INSIGHTS DATA =====")
print(insights)


# ==========================================
# 9. SAVE INSIGHTS
# ==========================================

insights.to_csv(
    "outputs/day_wise_train_insights.csv",
    index=False
)


# ==========================================
# 10. CREATE CORRELATION PLOT
# ==========================================

plt.figure(figsize=(10, 6))

plt.plot(
    weekdays,
    day_counts.values,
    marker="o"
)

plt.title("Train Count by Day of the Week")
plt.xlabel("Day of the Week")
plt.ylabel("Number of Trains")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "outputs/day_wise_train_correlation.png"
)

plt.show()


# ==========================================
# 11. FINAL INSIGHTS
# ==========================================

print("\n===== FINAL INSIGHTS =====")

print(
    f"1. {highest_day} has the highest number of train records "
    f"with {highest_count}."
)

print(
    f"2. {lowest_day} has the lowest number of train records "
    f"with {lowest_count}."
)

print(
    f"3. The difference between the highest and lowest day "
    f"is {difference} train records."
)

print(
    f"4. The difference is approximately "
    f"{percentage_difference:.2f}% relative to the lowest day."
)

print(
    "5. The correlation value describes the relationship between "
    "the numerical weekday order and train count; it should not "
    "be interpreted as a causal relationship."
)


# ==========================================
# 12. COMPLETION MESSAGE
# ==========================================

print("\n===== TASK 3.2 COMPLETED =====")

print("Insights saved to:")
print("outputs/day_wise_train_insights.csv")

print("\nCorrelation plot saved to:")
print("outputs/day_wise_train_correlation.png")