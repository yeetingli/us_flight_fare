from sklearn.metrics import mean_squared_error
import numpy as np

def evaluate_model(pipeline, X_train, y_train, X_val, y_val):
    """
    Function to calculate and print RMSE for both training and validation sets.
    
    Parameters:
    - pipeline: The fitted model pipeline
    - X_train: Training features
    - y_train: Training target values
    - X_val: Validation features
    - y_val: Validation target values
    
    Returns:
    - rmse_train: RMSE on the training set
    - rmse_val: RMSE on the validation set
    """
    # Predict on both training and validation sets
    y_train_pred = pipeline.predict(X_train)
    y_val_pred = pipeline.predict(X_val)
    
    # Calculate Mean Squared Error for both training and validation sets
    mse_train = mean_squared_error(y_train, y_train_pred)
    mse_val = mean_squared_error(y_val, y_val_pred)
    
    # Calculate RMSE
    rmse_train = np.sqrt(mse_train)
    rmse_val = np.sqrt(mse_val)
    
    # Print RMSE for both sets
    print(f'Training RMSE: {rmse_train}')
    print(f'Validation RMSE: {rmse_val}')
    
    return rmse_train, rmse_val
