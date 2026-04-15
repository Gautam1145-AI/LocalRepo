# Real-Time Weather Data Streaming Pipeline

## Overview

This project builds a near real-time weather data pipeline using a public weather API. It fetches live weather data at regular intervals, stores it in a database / CSV, and displays trends on a dashboard.

## Features

* Fetch live weather data using API
* Parse JSON responses
* Store weather records over time
* Visualize temperature and humidity trends
* Streamlit dashboard for monitoring

## Tech Stack

* Python
* Requests
* Pandas
* SQLite / CSV
* Streamlit

## Project Structure

```bash id="z8zc4c"
weather-streaming-pipeline/
├── data/
│   └── weather_data.csv
├── scripts/
│   └── fetch_weather.py
├── dashboard/
│   └── app.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. Clone the repository:

```bash id="6u7f0f"
git clone <your-repo-link>
```

2. Install dependencies:

```bash id="l89ccq"
pip install -r requirements.txt
```

3. Add your API key in:

```bash id="znwkp6"
scripts/fetch_weather.py
```

4. Run weather fetch script:

```bash id="amrtyf"
python scripts/fetch_weather.py
```

5. Run Streamlit dashboard:

```bash id="2h1xv8"
streamlit run dashboard/app.py
```

## Output

* Live weather data updates
* Temperature and humidity trends dashboard
* Historical weather records

## Learning Outcomes

* API data ingestion
* Near real-time data processing
* Scheduling and automation basics
* Dashboard creation

## Resume Points

* Built near real-time weather data pipeline using API
* Automated live data collection and storage
* Created dashboard for weather trend monitoring
