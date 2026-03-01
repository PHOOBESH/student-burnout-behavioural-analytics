import pandas as pd

# Load trigger-enriched data
df = pd.read_csv("student_behaviour_with_triggers.csv")

# -----------------------------
# Intervention Logic
# -----------------------------
def recommend_intervention(risk_level):
    if risk_level == "Low":
        return "Send productivity nudges and study tips"

    elif risk_level == "Medium":
        return "Schedule academic counselor check-in"

    else:
        return "Immediate advisor and mental health support"

df["recommended_intervention"] = df["burnout_risk_level"].apply(recommend_intervention)

# Save final dataset
df.to_csv("final_student_risk_output.csv", index=False)

print("Intervention recommendations added.")