import pandas as pd
from sklearn.model_selection import train_test_split
import os

from data_processing import clean_data
from model import train_model, save_model

# Define file paths
raw_data_path = '../data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv'
model_path = os.path.join('models', 'churn_predictor.joblib')

def run_training_pipeline():
    """
    Runs the full training pipeline to clean data, train a model, and save it.
    """
    # Load raw data
    df = pd.read_csv(raw_data_path)

    # Drop the customerID column here, before cleaning and encoding
    #df.drop('customerID', axis=1, inplace=True)

    # Clean and encode the data
    df_encoded = clean_data(df)

    # Separate features (X) and target (y)
    # We need to drop the 'customerID' and 'Churn' columns after one-hot encoding
    # Let's assume you've already handled this in clean_data.py
    X = df_encoded.drop(['Churn_numeric', 'Churn'], axis=1)
    y = df_encoded['Churn_numeric']

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    best_model = train_model(X_train, y_train)

    # Save the model
    save_model(best_model, model_path)

if __name__ == "__main__":
    run_training_pipeline()