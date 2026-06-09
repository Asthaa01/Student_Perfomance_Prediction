import joblib
import numpy as np

model = joblib.load("student_model.pkl")

print("Student Performance Prediction System")
print("------------------------------------")

try:
    study_hours = float(input("Study Hours Per Day: "))
    attendance = float(input("Attendance Percentage: "))
    sleep_hours = float(input("Sleep Hours: "))
    social_media = float(input("Social Media Hours: "))
    previous_score = float(input("Previous Exam Score: "))
    activities = int(input("Participation in Activities (0/1): "))
    internet_usage = float(input("Internet Usage Hours: "))

except ValueError:
    print("Invalid input!")
    exit()

features = np.array([[
    study_hours,
    attendance,
    sleep_hours,
    social_media,
    previous_score,
    activities,
    internet_usage
]])

prediction = model.predict(features)

print("\nPredicted Final Exam Score:")
print(round(prediction[0], 2))