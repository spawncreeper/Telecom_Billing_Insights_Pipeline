# Telecom Billing Insights Pipeline

This project is a comprehensive **data pipeline** designed to analyze telecom customer data, identify key performance indicators (KPIs), and predict customer churn. It evolved from a descriptive analysis of past trends into a powerful, reusable data product that leverages **machine learning** and **explainable AI**.

---

## 📈 Project Evolution

This project was built iteratively, demonstrating a complete data science workflow.

### **Version 1: Descriptive Analytics**
- **Objective:** Understand past customer behavior and business performance.  
- **Key Achievements:**  
  - Performed data cleaning  
  - Calculated KPIs like **ARPU (Average Revenue Per User)** and **churn rate**  
  - Identified key insights from historical data  

### **Version 2: Predictive Analytics**
- **Objective:** Forecast future customer behavior to enable proactive business decisions.  
- **Key Achievements:**  
  - Built and trained a **Random Forest Classifier** to predict churn  
  - Evaluated performance with a **confusion matrix** to assess business impact  

### **Version 3: Explainable AI (XAI)**
- **Objective:** Improve accuracy, trust, and transparency for non-technical stakeholders.  
- **Key Achievements:**  
  - Used **hyperparameter tuning** and **SMOTE balancing** to enhance performance  
  - Applied **SHAP** to explain individual churn predictions  

### **Version 4: Reusable Data Product**
- **Objective:** Transform into a portable, user-friendly tool.  
- **Key Achievements:**  
  - Modularized code into a `src/` directory  
  - Managed dependencies with `requirements.txt`  
  - Packaged the pipeline into a **standalone executable (.exe)** using **PyInstaller**  

---

## ⚡ Key Features
- **Automated Data Processing**: Cleans and engineers features automatically.  
- **KPI Dashboards**: Visualizations for churn rate by contract type, ARPU, etc.  
- **Predictive Churn Model**: Fine-tuned ML model for customer churn prediction.  
- **Explainable AI**: SHAP explanations for model predictions.  
- **Portable Executable**: Run the tool anywhere with a single `.exe` file.  

---

## 🚀 How to Run the Project

### **Setup**
1. Clone the repository:
   ```bash
   git clone https://github.com/spawncreeper/Telecom_Billing_Insights_Pipeline.git
   cd Telecom_Billing_Insights_Pipeline
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
3. Train and save the model:
    ```bash
    python src/train_and_save.py
    
This generates the model file: `src/models/churn_predictor.joblib`, which the main executable needs.

## Using the Executable
To use the standalone tool, navigate to the dist folder and run the executable from your terminal with a new CSV file:
``` bash
# Example command for a new data file
./main.exe --file "path/to/your/company/data.csv" --output "analysis_results"
```
The application will process the data, make predictions, and save a summary report and the full dataset with predictions to the specified output folder.

## 📂Project Structure
```bash
.
├── dist/
├── data/
│   ├── raw/
│   └── processed/
├── reports/
├── src/
│   ├── data_processing.py
│   ├── model.py
│   ├── analysis.py
│   └── models/
│       └── churn_predictor.joblib
├── main.py
├── notebooks/
├── README.md
└── requirements.txt
```
**File and Folder Descriptions**
- `dist/`: This directory contains the final, standalone executable (`main.exe`) created by PyInstaller. This is the only file users need to run your data product.

- `data/`: This folder is for managing your data.

    - `raw/`: Stores the original, untouched source data (`WA_Fn-UseC_-Telco-Customer-Churn.csv`).

    - `processed/`: Holds cleaned and processed data files (if you save them during the pipeline).

- `reports/`: This is where all the generated reports, charts, and output files will be saved.

- `src/`: The heart of your project's code. This folder contains all the reusable Python modules.

    - `data_processing.py`: Contains all the functions for data cleaning, preprocessing, and feature engineering.

    - `model.py`: Houses the logic for training, saving, and loading your machine learning model.

    - `analysis.py`: Includes functions for calculating KPIs, generating visualizations, and creating the final report content.

    - `models/`: Stores the serialized (`.joblib`) machine learning model after it has been trained.

- `main.py`: The entry point for your entire application. This script uses the `argparse` library to handle command-line arguments and orchestrates the calls to your `src/` modules.

- `notebooks/`: Contains all the original Jupyter Notebooks that document the exploratory data analysis, model development, and testing process.

- `requirements.txt`: A text file that lists all the Python dependencies required to run the project, ensuring a reproducible environment.

- `README.md`: This file, which provides an overview of the project, its features, and instructions on how to use it.

## 🛠️Technologies Used
- Python: Core programming language.

- Pandas: Data manipulation and analysis.

- Scikit-learn: Machine learning and model evaluation.

- SHAP: Model explainability.

- Plotly: Interactive data visualizations.

- PyInstaller: Packaging the project into a standalone executable.