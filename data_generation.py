import numpy as np
import pandas as pd

np.random.seed(42)

n_students = 500

data = {
    "student_id": range(1, n_students + 1),
    
    # Behavioural inputs
    "lms_logins_per_week": np.random.randint(1, 30, n_students),
    "avg_assignment_delay_days": np.round(np.random.uniform(0, 7, n_students), 2),
    "attendance_percentage": np.random.randint(50, 100, n_students),
    "activity_diversity": np.random.randint(1, 6, n_students),
    "night_activity_ratio": np.round(np.random.uniform(0, 1, n_students), 2)
}

df = pd.DataFrame(data)

df.head()

df.to_csv("student_behaviour_data.csv", index=False)