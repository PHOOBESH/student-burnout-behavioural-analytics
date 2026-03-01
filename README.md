Behavioural Drift–Based Student Burnout & Dropout Risk Prediction System

Problem Statement:Early Detection of Student Burnout & Dropout Risk

Universities often detect academic issues only after students’ performance has already declined. However, behavioural signals such as reduced LMS activity, delayed submissions, and declining engagement patterns appear much earlier. Detecting these early indicators enables timely intervention and prevents burnout-driven dropouts.

Objective:

To build a behavioural analytics system that:

-> Predicts student burnout risk (Low / Medium / High)

-> Identifies procrastination and silent disengagement patterns

-> Explains key behavioural triggers

-> Recommends appropriate intervention strategies

The system focuses on early, explainable, and actionable detection, rather than post-failure analysis.

Core Idea:

Instead of relying solely on academic performance, this system detects behavioural drift — deviations from healthy engagement patterns to identify:

-> Burnout risk

-> Chronic procrastination

-> Silent dropout tendencies

This allows universities to intervene before academic failure occurs.


Dataset Description :

Dataset Type: Synthetic (Simulated)

Reason for Using Synthetic Data:

Real student behavioural data is sensitive and restricted due to privacy concerns.And for hackathons short period of time cnnot collect primary data.Therefore, a synthetic dataset was generated using realistic behavioural assumptions aligned with academic environments.


Dataset Size : 500 student records


Feature	Description:
student_id - Unique student identifier
lms_logins_per_week  - Weekly LMS login frequency
avg_assignment_delay_days - Average delay in assignment submission
attendance_percentage -	Attendance consistency
activity_diversity - Variety of LMS activities
night_activity_ratio -	Proportion of late-night activity

Feature Engineering (Behavioural Logic) :

The following behavioural indicators were engineered:

1) Behavioural Drift Score

Measures deviation from healthy academic routines using:

-Reduced LMS activity

-Increased assignment delays

-Attendance decline

-Reduced activity diversity

2) Procrastination Index

Captures procrastination tendencies using:

-Assignment delay duration

-Night-time activity patterns

3) Silent Dropout Indicator

Identifies disengagement without formal dropout through:

-Very low LMS activity

-Minimal engagement diversity

These features are interpretable, behaviour-driven, and explainable.

Predictive Model:

Model Used : Random Forest Classifier

Reason for Model Choice :

-> Handles non-linear behavioural patterns
-> Robust to noise in synthetic data
-> Maintains interpretability

Target Output:

burnout_risk_level: Low / Medium / High

Model Performance:

The model achieved strong performance across all classes:

Overall Accuracy: ~96%

Balanced precision and recall across risk levels

No direct misclassification between extreme risk categories (Low ↔ High)

This confirms that behavioural patterns are being captured effectively.

Explainability: Behavioural Triggers

For each student, the system provides human-readable explanations, such as:

-“Significant behavioural routine deviation”

-“Chronic assignment procrastination”

-“Silent disengagement behaviour”

-“Stable academic behaviour”

This ensures transparency and trust in predictions.

Intervention Recommendation Engine:

Each risk level is mapped to an actionable intervention:

Low Risk Level  - Productivity nudges & study tips
Medium Risk Level  - Academic counselor check-in
High Risk Level  - Immediate advisor & mental health support

This converts predictions into decision intelligence.

