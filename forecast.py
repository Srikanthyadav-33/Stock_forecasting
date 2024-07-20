import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

def prepare_data(file_path):
    data = pd.read_csv(file_path, index_col='date', parse_dates=True)
    data = data[['4. close']]  # Selecting only the '4. close' column
    data['Prediction'] = data['4. close'].shift(-30)  # Creating a column for the shifted close prices
    return data

def train_model(data):
    X = np.array(data.drop(['Prediction'], axis=1))[:-30]  # Dropping the 'Prediction' column correctly
    y = np.array(data['Prediction'])[:-30]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)  # Adding random_state for reproducibility
    model = LinearRegression().fit(X_train, y_train)
    return model, X_test, y_test

def predict_future(data, model):
    X_future = np.array(data.drop(['Prediction'], axis=1))[-30:]  # Using axis=1 to drop the 'Prediction' column
    return model.predict(X_future)

if __name__ == "__main__":
    file_path = 'GOOGL_intraday.csv'  # Adjust the path to your actual CSV file
    data = prepare_data(file_path)
    model, X_test, y_test = train_model(data)
    predictions = predict_future(data, model)
    
    # Plotting the results
    data['4. close'].plot(figsize=(10, 6), label='Actual Close Price')
    plt.plot(data.index[-30:], predictions, color='red', label='Predicted Close Price')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.title('Actual vs Predicted Close Price')
    plt.legend()
    plt.grid(True)
    plt.show()
