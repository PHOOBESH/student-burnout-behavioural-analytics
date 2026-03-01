import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ast

st.set_page_config(
    page_title="Student Burnout Behavioural Analytics",
    layout="wide"
)

st.title("🎓 Student Burnout & Dropout Risk Analytics Dashboard")
st.markdown(
    """
    This dashboard provides **behavioural insights** into student burnout,
    procrastination, and silent disengagement using explainable analytics.
    """
)


@st.cache_data
def load_data():
    return pd.read_csv("final_student_risk_output.csv")

df = load_data()

st.sidebar.header("🔎 Filters")
risk_filter = st.sidebar.multiselect(
    "Select Risk Level",
    options=df["burnout_risk_level"].unique(),
    default=df["burnout_risk_level"].unique()
)

filtered_df = df[df["burnout_risk_level"].isin(risk_filter)]


st.subheader("📌 Key Risk Indicators")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Students", len(filtered_df))
col2.metric("High Risk Students", (filtered_df["burnout_risk_level"] == "High").sum())
col3.metric("Medium Risk Students", (filtered_df["burnout_risk_level"] == "Medium").sum())
col4.metric("Low Risk Students", (filtered_df["burnout_risk_level"] == "Low").sum())


st.subheader("📊 Burnout Risk Distribution")

fig1, ax1 = plt.subplots()
filtered_df["burnout_risk_level"].value_counts().plot(kind="bar", ax=ax1)
ax1.set_xlabel("Risk Level")
ax1.set_ylabel("Number of Students")
ax1.set_title("Distribution of Burnout Risk Levels")
st.pyplot(fig1)


st.subheader("📈 Behavioural Feature Comparison")

features = [
    "burnout_risk_score"
]

fig2, ax2 = plt.subplots()
sns.boxplot(
    data=filtered_df,
    x="burnout_risk_level",
    y="burnout_risk_score",
    ax=ax2
)
ax2.set_title("Burnout Risk Score by Risk Level")
st.pyplot(fig2)


st.subheader("📊 Average Behavioural Metrics by Risk Level")

metrics = [
    "burnout_risk_score"
]

avg_metrics = (
    df.groupby("burnout_risk_level")[metrics]
    .mean()
    .reset_index()
)

fig, ax = plt.subplots()
avg_metrics.set_index("burnout_risk_level").plot(
    kind="bar",
    ax=ax
)

ax.set_ylabel("Average Value")
ax.set_title("Average Behavioural Metrics by Risk Level")
st.pyplot(fig)

import ast

st.subheader("🔥 Most Common Behavioural Triggers")

# Convert stringified lists to actual lists
df["behavioural_triggers"] = df["behavioural_triggers"].apply(
    lambda x: ast.literal_eval(x) if isinstance(x, str) else x
)

# Explode triggers into separate rows
trigger_df = df.explode("behavioural_triggers")

# Count triggers
trigger_counts = (
    trigger_df["behavioural_triggers"]
    .value_counts()
    .reset_index()
)

trigger_counts.columns = ["Trigger", "Count"]

st.bar_chart(trigger_counts.set_index("Trigger"))


st.subheader("🚨 High Risk Behaviour Analysis")

high_risk_df = df[df["burnout_risk_level"] == "High"]

if not high_risk_df.empty:
    st.write("Common behavioural triggers among **High Risk** students:")
    st.dataframe(
        high_risk_df["behavioural_triggers"]
        .value_counts()
        .reset_index()
        .rename(columns={"index": "Trigger", "behavioural_triggers": "Count"})
    )
else:
    st.write("No high-risk students selected.")


st.subheader("👤 Student-Level Risk Analysis")

student_id = st.selectbox(
    "Select Student ID",
    df["student_id"].unique()
)

student = df[df["student_id"] == student_id].iloc[0]

colA, colB, colC = st.columns(3)
colA.metric("Risk Level", student["burnout_risk_level"])
colB.metric("Risk Score", int(student["burnout_risk_score"]))
colC.metric("Intervention", student["recommended_intervention"])

st.markdown("### Behavioural Triggers")
st.write(student["behavioural_triggers"])


st.subheader("📄 Dataset Preview")
st.dataframe(df.head(15))