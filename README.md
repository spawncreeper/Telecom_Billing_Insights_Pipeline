# Telecom Billing Insights Pipeline

This project aims to build a data pipeline to analyze telecom billing data. The goal is to provide actionable insights by calculating key performance indicators (KPIs) like Average Revenue Per User (ARPU) and churn rate, and visualizing them on a dashboard.

### Project Structure

- **`notebooks/`**: Contains Jupyter Notebooks for data ingestion, cleaning, KPI calculation, and dashboard creation.
- **`data/`**: Stores raw and processed datasets.
    - **`raw/`**: The original, untouched source data (`WA_Fn-UseC_-Telco-Customer-Churn.csv`).
    - **`processed/`**: Cleaned datasets that will be used for analysis.
- **`reports/`**: Final reports or generated dashboards.
- **`README.md`**: Project documentation.

### Technologies Used

- Python
- Pandas for data manipulation
- Plotly for data visualization