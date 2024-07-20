# visualize_data.py
import pandas as pd
import matplotlib.pyplot as plt

def plot_stock_data(file_path):
    data = pd.read_csv(file_path, index_col='date', parse_dates=True)
    data['4. close'].plot(title='Stock Close Prices', figsize=(10, 6))
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.show()

if __name__ == "__main__":
    file_path = 'GOOGL_intraday.csv'  # Change this to the path of your CSV file
    plot_stock_data(file_path)
