import pandas as pd

df = pd.read_csv("data/student_performance.csv")

print(df.head())
print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nSummary Statistics:")
print(df.describe())
print(
    df[['StudyHoursPerDay', 'FinalExamScore']].corr()
)
print(
    df[['AttendancePercentage', 'FinalExamScore']].corr()
)
print(
    df[['SleepHours', 'FinalExamScore']].corr()
)
print(
    df[['SocialMediaHours', 'FinalExamScore']].corr()
)
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8,6))

sns.scatterplot(
    x='StudyHoursPerDay',
    y='FinalExamScore',
    data=df
)

plt.title("Study Hours vs Final Exam Score")

plt.show()
plt.figure(figsize=(10,8))

sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    cmap='coolwarm'
)

plt.title("Correlation Heatmap")

plt.show()
activity_scores = (
    df.groupby(
        'ParticipationInActivities'
    )['FinalExamScore'].mean()
)

activity_scores.plot(
    kind='bar',
    color=['red', 'green']
)

plt.title(
    'Average Score by Activity Participation'
)

plt.xlabel('Participation (0=No,1=Yes)')
plt.ylabel('Average Score')

plt.show()
