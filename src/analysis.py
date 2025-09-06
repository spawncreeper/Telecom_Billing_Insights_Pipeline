import pandas as pd
import plotly.express as px

def calculate_kpis(df):
    """
    Calculates key performance indicators.

    Args:
        df (pd.DataFrame): The DataFrame with raw data.

    Returns:
        dict: A dictionary containing the calculated KPIs.
    """
    overall_arpu = df['MonthlyCharges'].mean()
    overall_churn_rate = (df['Churn'] == 'Yes').mean() * 100
    
    churn_by_contract = df.groupby('Contract')['Churn'].apply(lambda x: (x == 'Yes').mean()) * 100
    arpu_by_churn = df.groupby('Churn')['MonthlyCharges'].mean()

    return {
        'overall_arpu': overall_arpu,
        'overall_churn_rate': overall_churn_rate,
        'churn_by_contract': churn_by_contract,
        'arpu_by_churn': arpu_by_churn
    }

def generate_report(kpis, fig1, fig2):
    """
    Generates a Markdown report string with KPIs and visualizations.

    Args:
        kpis (dict): A dictionary of calculated KPIs.
        fig1_path (str): File path to the first chart image.
        fig2_path (str): File path to the second chart image.

    Returns:
        str: The Markdown report content.
    """
    report_md = f"""
# Telecom Billing Insights Report

This report provides key insights from customer billing data, helping to improve decision-making and business strategy.

## Key Performance Indicators (KPIs)

* **Overall Churn Rate**: {kpis['overall_churn_rate']:.2f}%
* **Overall ARPU**: ${kpis['overall_arpu']:.2f}

---

## Churn by Contract Type

![Churn Rate by Contract Type](../reports/churn_by_contract.png)
... (rest of your markdown report)
"""
    return report_md