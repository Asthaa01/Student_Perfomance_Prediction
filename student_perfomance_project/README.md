Student Performance Analysis & Prediction System

📌 Project Overview
This project predicts student final exam scores based on study habits and lifestyle factors using Machine Learning.

---

📊 Dataset
- Synthetic dataset of 1000 students
- Features include:
  - Study Hours
  - Attendance
  - Sleep Hours
  - Social Media Usage
  - Previous Exam Score
  - Participation in Activities
  - Internet Usage

---

🧠 Machine Learning Model
- Algorithm: Linear Regression
- Train-Test Split: 80/20
- Target: Final Exam Score

---

📈 Model Performance
(Add your actual values here after running model_training.py)

- MAE: 3.9158947167187086
- RMSE: 4.865136938009764
- R² Score: 0.8701495139367478

---

 📊 Visualizations
- Study Hours vs Final Score (Scatter Plot)
- Correlation Heatmap
- Activities vs Score (Bar Chart)

---

⚙️ How to Run the Project

1. Install dependencies:
pip install pandas numpy matplotlib seaborn scikit-learn joblib

2. Generate dataset:
python dataset_generator.py

3. Train model:
python model_training.py

4. Run prediction system:
python prediction_system.py

 * Key Insights
>Study hours positively affect exam scores.
>Attendance has a strong impact on performance.
>Previous exam scores are the strongest predictor.
>High social media usage tends to reduce scores.
>Random Forest achieved high prediction accuracy.

🎯 Outcome
The system predicts student exam performance based on input values.
