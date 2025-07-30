""" Project: Temperature plotter"""

import matplotlib.pyplot as plt
import pandas as pd

def load_data(file_path):
    "load temperature data from CSV file"
    try:
        data = pd.read_csv(file_path, parse_dates= ['Date'])
        print("Data loaded successfully")
        return data
    except Exception as e:
        print("Error loading data:", e)
        return None

def plot_temperature(data, save_file = None):
    "plot temperature trends with options for rolling average and anomalies"
    
    # add rolling average
    data['7-Day Average'] = data['Temperature'].rolling(window = 7).mean()

    # identify anomalies
    mean_temp = data['Temperature'].mean()
    std_temp = data['Temperature'].std()
    data['Anomaly'] = (data['Temperature'] > mean_temp + 2 * std_temp) | (data['Temperature'] < mean_temp - 2 * std_temp)

    # plot
    plt.style.use("seaborn-v0_8-darkgrid")
    plt.figure(figsize= (10, 6))
    plt.plot(data['Date'], data['Temperature'], label = "Daily Temperature", color = "blue")
    plt.plot(data['Date'], data['7-Day Average'], label = "7-Day average", linestyle = "--", color = 'orange')
    plt.scatter(data[data['Anomaly']]['Date'], data[data['Anomaly']]['Temperature'], color = 'red', label = "Anomalies")
    plt.title("Temperature Trends")
    plt.xlabel("Date")
    plt.ylabel("Temperature (C)")
    plt.grid(True)
    plt.legend()

    # save or show plot
    if save_file:
        plt.savefig(save_file)
        print(f"plot saved as {save_file}")
    else:
        plt.show()

def main():
    print("Welcome to the temperature plotter!")

    # load data 
    file_path = input("Enter the path to your temperature CSV file: ")
    data = load_data(file_path)
    if data is None:
        return
    
    # plot temperature
    save_choice = input("Do you want to save the plot? (y/n):").lower()
    if save_choice == "y":
        file_name = input("Enter the file name (e.g., temperature_plot.png): ")
        plot_temperature(data, save_file= file_name)

    else:
        plot_temperature(data)

if __name__ == "__main__":
    main()