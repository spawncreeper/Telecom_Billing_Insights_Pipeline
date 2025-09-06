import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
import joblib

def train_model(X_train, y_train):
    """
    Trains a RandomForestClassifier model using GridSearchCV.

    Args:
        X_train (pd.DataFrame): The training features.
        y_train (pd.Series): The training labels.

    Returns:
        The best trained model.
    """
    rf = RandomForestClassifier(random_state=42)
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [10, 20, None],
        'min_samples_split': [2, 5, 10]
    }
    grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, scoring='accuracy', n_jobs=-1)
    grid_search.fit(X_train, y_train)
    return grid_search.best_estimator_

def save_model(model, file_path):
    """
    Saves a trained model to a file.

    Args:
        model: The trained model to save.
        file_path (str): The path to save the model file.
    """
    joblib.dump(model, file_path)
    print(f"Model saved to {file_path}")

def load_model(file_path):
    """
    Loads a trained model from a file.

    Args:
        file_path (str): The path to the model file.

    Returns:
        The loaded model.
    """
    return joblib.load(file_path)