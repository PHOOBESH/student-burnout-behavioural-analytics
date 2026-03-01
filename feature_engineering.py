import pandas as pd

# Load dataset
df = pd.read_csv("student_behaviour_data.csv")

# -----------------------------
# Behavioural Drift Score
# -----------------------------
df["behavioural_drift_score"] = (
    (30 - df["lms_logins_per_week"]) * 0.4 +
    df["avg_assignment_delay_days"] * 0.3 +
    (100 - df["attendance_percentage"]) * 0.2 +
    (5 - df["activity_diversity"]) * 0.1
)

# -----------------------------
# Procrastination Index
# -----------------------------
df["procrastination_index"] = (
    df["avg_assignment_delay_days"] * 0.6 +
    df["night_activity_ratio"] * 0.4
)

# -----------------------------
# Silent Dropout Indicator
# -----------------------------
df["silent_dropout_indicator"] = (
    (df["lms_logins_per_week"] < 8).astype(int) +
    (df["activity_diversity"] < 2).astype(int)
)

# Save updated dataset
df.to_csv("student_behaviour_features.csv", index=False)

print("Feature engineering completed and saved.")