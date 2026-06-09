import pandas as pd
import numpy as np

np.random.seed(42)

num_students = 1000

student_ids = np.arange(1, num_students + 1)

study_hours = np.random.uniform(1, 8, num_students)

attendance = np.random.uniform(50, 100, num_students)

sleep_hours = np.random.uniform(4, 10, num_students)

social_media = np.random.uniform(0, 6, num_students)

previous_score = np.random.uniform(40, 100, num_students)

activities = np.random.randint(0, 2, num_students)

internet_usage = np.random.uniform(1, 10, num_students)

final_score = (
    study_hours * 4
    + attendance * 0.3
    + sleep_hours * 2
    - social_media * 1.5
    + previous_score * 0.5
    + activities * 3
    + np.random.normal(0, 5, num_students)
)

final_score = np.clip(final_score, 0, 100)

df = pd.DataFrame({
    "StudentID": student_ids,
    "StudyHoursPerDay": study_hours,
    "AttendancePercentage": attendance,
    "SleepHours": sleep_hours,
    "SocialMediaHours": social_media,
    "PreviousExamScore": previous_score,
    "ParticipationInActivities": activities,
    "InternetUsageHours": internet_usage,
    "FinalExamScore": final_score
})

df.to_csv("data/student_performance.csv", index=False)

print("Dataset Created Successfully!")
print(df.head())