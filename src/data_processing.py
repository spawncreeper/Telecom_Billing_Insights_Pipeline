import pandas as pd

def clean_data(df):
    """
    Cleans the raw data by handling missing values, converting data types,
    and creating new features.

    Args:
        df (pd.DataFrame): The raw DataFrame.

    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """

    # Drop the customerID column as it's not needed for the model
    df.drop('customerID', axis=1, inplace=True)

    # Convert 'TotalCharges' to numeric and handle missing values
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df.dropna(inplace=True)

    # Create the 'Churn_numeric' column
    df['Churn_numeric'] = df['Churn'].apply(lambda x: 1 if x == 'Yes' else 0)

    # One-hot encode categorical features (except the target)
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    # Remove 'Churn' and 'customerID' from the list of columns to encode
    categorical_cols.remove('Churn') 
    #categorical_cols.remove('customerID') 

    df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    return df_encoded