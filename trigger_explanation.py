import pandas as pd

# Load labeled data
df = pd.read_csv("student_behaviour_labeled.csv")

# -----------------------------
# Behavioural Trigger Logic
# -----------------------------
def explain_triggers(row):
    triggers = []

    if row["behavioural_drift_score"] > 20:
        triggers.append("Significant behavioural routine deviation")

    if row["procrastination_index"] > 3:
        triggers.append("Chronic assignment procrastination")

    if row["silent_dropout_indicator"] >= 1:
        triggers.append("Silent disengagement behaviour")

    if not triggers:
        triggers.append("Stable academic behaviour")

    return triggers

df["behavioural_triggers"] = df.apply(explain_triggers, axis=1)

# Save output
df.to_csv("student_behaviour_with_triggers.csv", index=False)

print("Behavioural trigger explanation completed.")