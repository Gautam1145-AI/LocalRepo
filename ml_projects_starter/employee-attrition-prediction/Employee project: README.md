# Employee Attrition Prediction

## Overview

This project predicts whether an employee is likely to leave a company based on HR-related features such as age, monthly income, overtime, job role, and years at company.

## Features

* Data cleaning and preprocessing
* Handling missing values
* Label encoding for categorical data
* Feature scaling
* Random Forest classification model
* Streamlit web app for live predictions

## Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Joblib

## Project Structure

```bash
employee-attrition-prediction/
├── data/
├── models/
├── src/
│   ├── train.py
│   └── predict.py
├── app.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. Clone the repository:

```bash
git clone <your-repo-link>
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Add dataset:

* Place employee attrition dataset inside:

```bash
data/employee_attrition.csv
```

4. Train the model:

```bash
python src/train.py
```

5. Run Streamlit app:

```bash
streamlit run app.py
```

## Output

* Predicts whether employee is likely to leave or stay.
* Useful for HR analytics and workforce planning.

## Learning Outcomes

* Classification workflow
* Feature engineering
* Model training and evaluation
* Web app deployment

## Resume Points

* Built an employee attrition prediction system using machine learning.
* Applied preprocessing, encoding, and Random Forest classification.
* Developed an interactive Streamlit app for prediction.
