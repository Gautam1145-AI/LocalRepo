# E-commerce Sales ETL Pipeline

## Overview

This project builds a batch ETL (Extract, Transform, Load) pipeline for e-commerce sales data. It extracts raw sales data from CSV files, cleans and transforms it, and loads the processed data into a SQL database for analysis.

## Features

* Extract raw sales data from CSV files
* Clean missing values and duplicates
* Convert date formats and standardize columns
* Load transformed data into SQL database
* Generate sales reports and insights

## Tech Stack

* Python
* Pandas
* SQLAlchemy
* SQLite / MySQL
* Jupyter Notebook (optional)

## Project Structure

```bash id="jlwmx1"
ecommerce-etl-pipeline/
├── data/
│   ├── sales.csv
│   ├── extracted_sales.csv
│   └── cleaned_sales.csv
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── sales.db
├── requirements.txt
└── README.md
```

## Setup Instructions

1. Clone the repository:

```bash id="0r5zri"
git clone <your-repo-link>
```

2. Install dependencies:

```bash id="w6ow0m"
pip install -r requirements.txt
```

3. Add raw sales dataset:

```bash id="rjlwm6"
data/sales.csv
```

4. Run ETL scripts:

```bash id="r6o9j4"
python scripts/extract.py
python scripts/transform.py
python scripts/load.py
```

## Output

* Cleaned and transformed sales data
* SQL database with structured sales records
* Sales analysis for revenue and trends

## Learning Outcomes

* Batch ETL pipeline design
* Data cleaning and transformation
* SQL database loading
* Business data analysis

## Resume Points

* Built batch ETL pipeline for e-commerce sales data
* Automated extraction, cleaning, and loading into SQL
* Improved understanding of data warehousing concepts
