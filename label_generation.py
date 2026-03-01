import pandas as pd

# Load feature-engineered data
df = pd.read_csv("student_behaviour_features.csv")

# ---------------------------------
# Burnout Risk Score (0–100 scale)
# ---------------------------------
df["burnout_risk_score"] = (
    df["behavioural_drift_score"] * 0.5 +
    df["procrastination_index"] * 20 +
    df["silent_dropout_indicator"] * 15
)

# Cap values at 100 for safety
df["burnout_risk_score"] = df["burnout_risk_score"].clip(0, 100)

# ---------------------------------
# Burnout Risk Level (Target Label)
# ---------------------------------
df["burnout_risk_level"] = pd.cut(
    df["burnout_risk_score"],
    bins=[0, 30, 60, 100],
    labels=["Low", "Medium", "High"]
)

# Save labeled dataset
df.to_csv("student_behaviour_labeled.csv", index=False)

print("Risk labeling completed and saved.")