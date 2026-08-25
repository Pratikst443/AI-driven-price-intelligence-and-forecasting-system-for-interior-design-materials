# BLUE – AI-Driven Price Intelligence & Forecasting System
Comparative Price Forecasting of Interior Design Products
Project Overview

BLUE is an AI-driven price intelligence and forecasting system developed to analyze historical pricing behaviour and forecast future prices of interior design products.

The system combines historical price analysis, statistical forecasting, machine learning, and interactive visualization into a single Streamlit-based dashboard.

The system focuses on four major interior-design product categories:

- Furniture
- Lighting
- Flooring
- Decor

Unique Value Proposition (UVP)

The Unique Value Proposition of BLUE is its ability to combine historical price intelligence and multi-model forecasting within a single interactive system.

Instead of relying only on historical price visualization or a single forecasting technique, BLUE enables users to:

Explore historical pricing behaviour
Compare prices across categories
Analyze price trends
Measure category-level growth and volatility
Forecast future prices
Compare the performance of multiple forecasting models
Generate analytical insights through an interactive dashboard

This provides a unified platform for understanding historical price behaviour and evaluating future price trends.

# 1. Project Objectives

The major objectives of BLUE are:

- To analyze historical prices of interior design products.
- To identify pricing trends across different product categories.
- To analyze category-level growth and price volatility.
- To forecast future product prices using multiple forecasting    approaches.
- To compare the predictive performance of Prophet, ARIMA, and GRU.
- To provide an interactive dashboard for exploring historical and forecasted price information.
- To generate analytical insights that support understanding of price behaviour.

# 2. Key Features

BLUE provides the following major capabilities:

- Interactive dataset exploration
- Category and sub-category based analysis
- Historical price trend visualization
- Category-level average price analysis
- CAGR analysis
- Price volatility analysis
- Average monthly return analysis
- Future price forecasting
- Forecast confidence intervals
- Multi-model performance comparison
- Interactive Streamlit dashboard
- Analytical insights
The dashboard is organized into dedicated modules for dataset exploration, historical analysis, forecasting, model comparison, and insights.

# 3. Forecasting Methodology

BLUE implements three forecasting approaches:

3.1 Prophet

Prophet is used as a time-series forecasting approach for predicting future prices. The forecasting output includes predicted values and forecast intervals.

3.2 ARIMA

ARIMA (AutoRegressive Integrated Moving Average) is used as a statistical time-series forecasting approach based on historical price observations.

3.3 GRU

GRU (Gated Recurrent Unit) is used as a neural-network-based forecasting approach for sequential price data.

The three approaches provide a basis for comparing statistical and neural-network-based forecasting performance.

# 4. Model Evaluation

The forecasting models are evaluated using two metrics:

Mean Absolute Error (MAE):
MAE measures the average absolute difference between actual and predicted values.

Root Mean Squared Error (RMSE):
RMSE measures the square root of the average squared prediction error and gives greater weight to larger errors.

For both metrics, lower values indicate better forecasting performance.

- Model Performance
| Model	 | MAE	   | RMSE   |
|Prophet |	307.79 | 361.22 | 
|GRU	 |  623.60 | 667.71 |
|ARIMA	 |  831.60 | 1008.82|

Based on the reported evaluation results, Prophet achieved the lowest MAE and RMSE among the evaluated models.

# 5. Dashboard Modules

The Streamlit application consists of the following modules.

5.1 Home
Provides an overview of the BLUE project and its purpose.

5.2 Dataset Explorer
Allows users to explore the interior design pricing dataset using category and sub-category filters.

5.3 Historical Analysis
The Historical Analysis module provides:

- Historical average price trends
- CAGR analysis
- Price volatility
- Average monthly returns

5.4 Forecasting
The Forecasting module allows users to select a category and sub-category and view future price forecasts.

Forecast results are loaded from the generated forecast CSV files stored under the data/forecast/ directory.

5.5 Model Comparison
The Model Comparison module compares Prophet, ARIMA, and GRU using MAE and RMSE.

5.6 Insights
The Insights module provides interpretation of important analytical and forecasting results.

# 6. Technology Stack
Programming Language:
Python

Framework:
Streamlit

Libraries:
- Pandas
- NumPy
- Plotly
- Prophet
- Statsmodels
- Scikit-learn
- TensorFlow

These dependencies are specified in the project's requirements.txt.

Development Tools:
- Visual Studio Code
- Google Colab
- Git
- GitHub

# 7. Project Architecture

The project follows a data-processing, forecasting, evaluation, and visualization workflow:

Raw / Historical Dataset
          │
          ▼
    Data Preprocessing
          │
          ▼
 Historical Price Analysis
          │
          ├───────────────┐
          ▼       ▼       ▼
     Prophet     GRU    ARIMA
          │       │        │
          └───────│────────┘
                  │
                  ▼
                 GRU
                  │
                  ▼
          Model Evaluation
          (MAE & RMSE)
                  │
                  ▼
        Forecast CSV Outputs
                  │
                  ▼
        Streamlit Dashboard
                  │
        ┌─────────┼──────────┐
        ▼         ▼          ▼
     Dataset   Historical  Forecasting
     Explorer   Analysis       │
                                ▼
                         Model Comparison
                                │
                                ▼
                           Insights

# 8. Project Structure
AI Forecasting Dashboard/
│
├── .gitignore
│
├── assets/
│
├── data/
│   ├── interior_design_prices.csv
│   ├── growth_summary.csv
│   ├── model_comparison.csv
│   ├── prophet_evaluation.csv
│   ├── arima_evaluation.csv
│   ├── gru_evaluation.csv
│   ├── future_summary.csv
│   ├── future_summary_next12m.csv
│   │
│   └── forecast/
│       ├── forecast_Artifical Plants.csv
│       ├── forecast_Beds.csv
│       ├── forecast_Ceiling Lights.csv
│       ├── ...
│       └── forecast_Wood.csv
│
├── Images/
│   └── BLUE.png
│
├── notebooks/
│   └── Blue-AI Driven Price Intelligence and
│       Forecasting System for Interior Design Materials.ipynb
│
├── pages/
│   ├── 1_Dataset_Explorer.py
│   ├── 2_Historical_Analysis.py
│   ├── 3_Forecasting.py
│   ├── 4_Model_Comparison.py
│   └── 5_Insights.py
│
├── Home.py
├── charts.py
├── utils.py
├── style.css
├── requirements.txt
└── README.md

The application uses utils.py to load the dataset, analysis summaries, model evaluations, and forecast outputs from the data directory.

# 9. Data and Forecast Outputs

The project stores the primary dataset and generated analytical outputs in the data/ directory.

The data directory contains:

- Historical interior-design pricing dataset
- Growth summary
- Model comparison results
- Prophet evaluation results
- ARIMA evaluation results
- GRU evaluation results
- Future summary data
- Individual sub-category forecast files

Forecast files are organized under:
data/forecast/

and are loaded dynamically by the Streamlit application based on the selected sub-category.

# 10. Installation
Prerequisites
Make sure the following are installed:
- Python
- pip
- Git

Clone the repository:

git clone https://github.com/Pratikst443/AI-driven-price-intelligence-and-forecasting-system-for-interior-design-materials.git

Navigate into the project directory:

cd AI-driven-price-intelligence-and-forecasting-system-for-interior-design-materials

Create and activate a virtual environment if required:

macOS / Linux:
python3 -m venv venv
source venv/bin/activate

Windows:
python -m venv venv
venv\Scripts\activate

Install the required dependencies:
pip install -r requirements.txt

The project's dependency file includes Streamlit, Pandas, NumPy, Plotly, Prophet, Statsmodels, Scikit-learn, and TensorFlow.

# 11. Running the Application

From the project root directory, run:

streamlit run Home.py

The Streamlit application will open in the browser.

The dashboard can then be used to navigate between:
- Dataset Explorer
- Historical Analysis
- Forecasting
- Model Comparison
- Insights

# 12. Forecasting Output

The forecasting module provides predicted future prices along with forecast intervals.

Forecast data contains:
- ds
- yhat
- yhat_lower
- yhat_upper

where:
- ds represents the forecast date.
- yhat represents the predicted price.
- yhat_lower represents the lower forecast bound.
- yhat_upper represents the upper forecast bound.

The dashboard visualizes the forecasted price trend and confidence interval. The forecasting chart implementation uses the yhat, yhat_lower, and yhat_upper fields.

# 13. Visualization

The dashboard uses Plotly for interactive visualizations.

Category-specific visualizations use a consistent project colour scheme:
- Furniture: Light Blue
- Lighting: Blue
- Flooring: Pink
- Decor: Red

The same category mapping is applied across category distribution, average-price, historical-trend, CAGR, volatility, and monthly-return visualizations.

The dashboard also provides interactive MAE and RMSE comparison charts for evaluating the forecasting models.

# 14. Notebook

The notebooks/ directory contains the Google Colab notebook used for the forecasting pipeline.

The notebook documents the workflow from data processing and analysis through forecasting and model evaluation.

The generated outputs from the forecasting pipeline are subsequently used by the Streamlit dashboard.

# 15. Reproducibility

To reproduce the dashboard:
1. Clone the GitHub repository.
2. Install the dependencies using requirements.txt.
3. Ensure the required data and generated forecast CSV files are available under the data/ directory.
4. Run the Streamlit application using:
streamlit run Home.py

The dashboard reads the stored datasets and forecast outputs using the project's utility functions.

# 16. Future Scope

Potential future improvements include:

- Incorporating additional forecasting models.
- Incorporating additional external factors that may influence product prices.
- Providing more granular forecasting at product level.
- Improving automated model selection.
- Adding additional interactive analytical features.
- Deploying the dashboard as an online application.

# 17. Conclusion

BLUE provides an integrated platform for analyzing and forecasting prices of interior design products.

By combining historical price analysis, multiple forecasting approaches, model evaluation, and interactive visualization, the system provides a consolidated environment for exploring price behaviour and future forecasts.

The evaluated results show that Prophet achieved the lowest MAE and RMSE among the three implemented forecasting models, making it the strongest-performing model in the reported evaluation.

## Repository

# GitHub Repository:
https://github.com/Pratikst443/AI-driven-price-intelligence-and-forecasting-system-for-interior-design-materials