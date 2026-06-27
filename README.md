# 💳 Credit Card Approval Prediction using Machine Learning

## 📌 Project Overview

This project predicts whether a customer's credit card application is likely to be approved based on demographic, financial, and employment information. The solution uses Machine Learning techniques to analyze applicant data and provides predictions through an interactive Flask web application.

The project demonstrates the complete Machine Learning workflow, including data preprocessing, exploratory data analysis (EDA), feature engineering, model training, evaluation, and deployment-ready web application development.

---

# 🚀 Features

* Exploratory Data Analysis (EDA)
* Data Cleaning & Preprocessing
* Missing Value Handling
* Feature Engineering
* Label Encoding of Categorical Features
* Feature Scaling using StandardScaler
* Class Imbalance Handling using SMOTE
* Multiple Machine Learning Models
* Model Performance Comparison
* Random Forest Model Selection
* Flask Web Application
* User-Friendly Prediction Interface

---

# 🛠️ Technologies Used

### Programming Language

* Python

### Machine Learning Libraries

* Scikit-learn
* XGBoost
* Imbalanced-learn (SMOTE)
* Pandas
* NumPy
* Joblib

### Data Visualization

* Matplotlib

### Web Framework

* Flask
* HTML
* CSS

---

# 📂 Dataset

The project uses two datasets:

* **Application Record Dataset**
* **Credit Record Dataset**

These datasets are merged using the customer ID to generate the final dataset for model training.

---

# 📊 Machine Learning Workflow

1. Load Dataset
2. Exploratory Data Analysis (EDA)
3. Handle Missing Values
4. Create Target Variable
5. Merge Datasets
6. Encode Categorical Features
7. Feature Scaling
8. Train-Test Split
9. Handle Class Imbalance using SMOTE
10. Train Multiple Models
11. Compare Model Performance
12. Save Best Model
13. Build Flask Web Application

---

# 🤖 Models Trained

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier
* XGBoost Classifier

After comparing the performance of all models, **Random Forest** was selected as the final model for deployment.

---

# 📈 Model Evaluation

The models were evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix
* Classification Report

Class imbalance was handled using **SMOTE (Synthetic Minority Over-sampling Technique)** to improve the prediction of minority-class samples.

---

# 📁 Project Structure

```text
Credit-Card_Approval_Prediction/
│
├── dataset/
│
├── models/
│   ├── model.pkl
│   ├── scaler.pkl
│   └── encoder.pkl
│
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_Preprocessing.ipynb
│   └── 03_Model_Training.ipynb
│
├── static/
│   ├── css/
│   ├── images/
│   └── js/
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── screenshots/
│
├── app.py
├── predict.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/Credit-Card_Approval_Prediction.git
```

Move into the project folder

```bash
cd Credit-Card_Approval_Prediction
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

Start the Flask application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

# 📸 Project Screenshots

Add your screenshots here.

### Home Page

```
screenshots/home_page.png
```

### Prediction Result

```
screenshots/approved_prediction.png
```

### Model Comparison

```
screenshots/accuracy_comparison.png
```

### Confusion Matrix

```
screenshots/confusion_matrix.png
```

---

# 🎯 Future Improvements

* Hyperparameter tuning
* Model deployment on cloud platforms
* Improved user interface
* Additional feature engineering
* Real-time prediction API
* Deep Learning-based models
* Explainable AI using SHAP or LIME

---

# 👨‍💻 Author

**Yerninti Tarun**

B.Tech Information Technology

Machine Learning | Artificial Intelligence | Full Stack Development

GitHub: https://github.com/tarun-4646

---

# ⭐ If you found this project useful, consider giving it a star!
