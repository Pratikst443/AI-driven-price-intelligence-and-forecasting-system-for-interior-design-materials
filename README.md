# BLUE – AI-Driven Price Intelligence & Forecasting System

## Comparative Price Forecasting of Interior Design Products

BLUE is an AI-driven price intelligence and forecasting system developed to analyze historical pricing behaviour and forecast future prices of interior design materials.

The system combines historical price analysis, statistical forecasting, machine learning, and interactive visualization into a single Streamlit-based dashboard.

---

## 1. Project Overview

Interior design products such as furniture, lighting, flooring, and decorative products can experience significant changes in price over time.

BLUE provides an integrated platform for:

- Exploring historical pricing data
- Comparing prices across categories
- Analyzing historical price trends
- Measuring category-level growth and volatility
- Forecasting future prices
- Comparing forecasting model performance
- Generating analytical insights

The system focuses on four major categories:

- Furniture
- Lighting
- Flooring
- Decor

---

## 2. Unique Value Proposition

The unique value proposition of BLUE is its ability to combine historical price intelligence and multi-model forecasting within a single interactive system.

Instead of only displaying historical prices or generating forecasts using one model, BLUE allows users to explore historical behaviour, evaluate price variability, generate future forecasts, and compare multiple forecasting approaches through one dashboard.

---

## 3. Forecasting Models

The project implements three forecasting approaches:

### Prophet

Prophet is used for time-series forecasting and provides predicted prices along with forecast intervals.

### ARIMA

ARIMA is used as a statistical time-series forecasting approach based on historical price observations.

### GRU

Gated Recurrent Unit (GRU) is used as a neural-network-based forecasting approach for sequential price data.

---

## 4. Model Evaluation

The forecasting models are evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

Lower values indicate better forecasting performance.

The final model comparison produced:

| Model   | MAE    | RMSE    |
| Prophet | 307.79 | 361.22  |
| GRU     | 623.60 | 667.71  |
| ARIMA   | 831.60 | 1008.82 |

Based on these evaluation results, Prophet achieved the lowest MAE and RMSE among the evaluated models.

---

## 5. Dashboard Modules

The Streamlit dashboard contains the following sections:

### Home

Provides an overview of the BLUE project and its purpose.

### Dataset Explorer

Allows users to explore the interior design pricing dataset using category and sub-category filters.

### Historical Analysis

Provides:

- Historical average price trends
- CAGR analysis
- Price volatility
- Average monthly returns

### Forecasting

Allows users to select a category and sub-category and view future price forecasts.

### Model Comparison

Compares Prophet, ARIMA, and GRU using MAE and RMSE.

### Insights

Provides interpretation of important analytical and forecasting results.

---

## 6. Project Structure


AI Forecasting Dashboard/
│
├── data/
│   ├── interior_design_prices.csv
│   ├── growth_summary.csv
│   ├── model_comparison.csv
│   ├── prophet_evaluation.csv
│   ├── arima_evaluation.csv
│   ├── gru_evaluation.csv
│   ├── future_summary_next12m.csv
│   └── forecast/
│
├── pages/
│   ├── 1_Dataset_Explorer.py
│   ├── 2_Historical_Analysis.py
│   └── 3_Forecasting.py
│   └── 4_Model_Comparison.py
│   └── 5_Insights.py
│
├── Home.py
├── charts.py
├── utils.py
├── style.css
├── requirements.txt
└── README.md