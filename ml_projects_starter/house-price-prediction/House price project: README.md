# House Price Prediction

## Overview

This project predicts house prices based on important housing features such as area, number of bedrooms, bathrooms, parking, and furnishing status.

## Features

* Data cleaning and preprocessing
* Missing value handling
* One-hot encoding
* Feature scaling
* Random Forest regression model
* Streamlit web app for price prediction

## Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Joblib

## Project Structure

```bash
house-price-prediction/
├── data/
├── models/
├── src/
│   └── train.py
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

* Place housing dataset inside:

```bash
data/housing.csv
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

* Predicts estimated house price.
* Useful for real estate analytics.

## Learning Outcomes

* Regression workflow
* Data preprocessing
* Model evaluation
* ML deployment basics

## Resume Points

* Developed a house price prediction system using regression techniques.
* Performed feature engineering and model optimization.
* Built a user-friendly Streamlit prediction interface.
