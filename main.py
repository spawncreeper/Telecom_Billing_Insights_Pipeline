import pandas as pd
import argparse
import os
import joblib

# Import your custom modules
from src.data_processing import clean_data
from src.analysis import calculate_kpis
from src.model import load_model

def run_pipeline(input_file, output_folder):
    """
    Runs the full data pipeline from file input to report generation.
    """
    # 1. Load the raw data
    try:
        df_raw = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
        return

    # 2. Process and clean the data
    print("Processing data...")
    df_cleaned = clean_data(df_raw)

    # 3. Calculate KPIs
    print("Calculating KPIs...")
    kpis = calculate_kpis(df_cleaned)

    # 4. Load the trained model
    print("Loading predictive model...")
    model_path = 'src/models/churn_predictor.joblib'
    model = load_model(model_path)

    # 5. Make predictions
    print("Making churn predictions...")
    # Prepare data for prediction by one-hot encoding
    df_pred = df_cleaned.drop(['Churn_numeric', 'Churn'], axis=1)
    # The columns need to be aligned with the training data
    # In a real product, you'd handle new columns gracefully. For now, we'll assume a similar structure.
    X_pred_encoded = pd.get_dummies(df_pred, drop_first=True)
    
    # Get the columns from the training data that the model expects
    training_columns = model.feature_names_in_
    # Align the new data's columns with the training data's columns, adding missing columns as zeros
    X_final = X_pred_encoded.reindex(columns=training_columns, fill_value=0)
    
    predictions = model.predict(X_final)
    
    # Add predictions back to the cleaned DataFrame
    df_cleaned['prediction'] = predictions

    # 6. Generate the report
    print("Generating report...")
    # This is where you would call a function to generate your Markdown or HTML report
    # For now, we'll just print the summary
    print("\n--- Final Report Summary ---")
    print(f"Overall Churn Rate: {kpis['overall_churn_rate']:.2f}%")
    print(f"Overall ARPU: ${kpis['overall_arpu']:.2f}")
    print(f"Number of predicted churns: {sum(predictions)}")

    # Ensure the output directory exists
    os.makedirs(output_folder, exist_ok=True)
    df_cleaned.to_csv(os.path.join(output_folder, 'processed_with_predictions.csv'), index=False)
    print(f"Full data with predictions saved to '{output_folder}'.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a data pipeline for telecom churn analysis.")
    parser.add_argument("--file", required=True, help="Path to the input CSV file.")
    parser.add_argument("--output", default="output", help="Path to the output folder for reports and data.")

    args = parser.parse_args()
    run_pipeline(args.file, args.output)