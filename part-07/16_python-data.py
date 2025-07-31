""" fetching real-time weather data 
    visualizing weather trends
    creating user friendly dashboard
    enhancing functionality with advanced features 
"""
import requests
import pandas as pd
import matplotlib.pyplot as plt

API_KEY = "YOUR_API_KEY"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# fetching real-time weather data
def fetch_weather_data(city):
    params = {
        "q": city, 
        "appid" : API_KEY,
        "units" : "metric"
    }

    response = requests.get(BASE_URL, params= params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data: ", response.status_code)
        return None

# displaying weather trends
def display_weather_data(data):
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Weather: {data['weather'][0]['description'].title()}")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind Speed: {data['wind']['speed']} m/s")

# visualizing weather trends
def plot_weather_trend(days, temperatures):
    plt.plot(days, temperatures, marker = "o", color = "blue")
    plt.title("Temperature Trend")
    plt.xlabel("Days")
    plt.ylabel("Temperature")
    plt.grid()
    plt.show()

# enhancing functionality with advanced features
def compare_weather(cities):
    temps = []
    for city in cities:
        data = fetch_weather_data(city)
        if data:
            temps.append((city, data['main']['temp']))
    
    # plot comparison
    city_names = [t[0] for t in temps]
    city_temps = [t[1] for t in temps]
    plt.bar(city_names, city_temps, color = 'skyblue')
    plt.title("Temperature Comparison")
    plt.xlabel("City")
    plt.ylabel("Temperature (C)")
    plt.show()

# creating user friendly dashboard
def main():
    print("Welcome  to the gloabal weather dashboard")
    city = input("Enter the city name: ")

    weather_data = fetch_weather_data(city)
    if weather_data:
        display_weather_data(weather_data)

        # simulated data for trend visualization
        days = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5']
        temperatures = [22, 24, 23, 25, 26]
        plot_weather_trend(days, temperatures)
    else:
        print("Could not retrieve weather data. Please try again!")

if __name__ == "__main__":
    main()
    compare_weather(["Atlanta", "Pune", "London", "Ohio"])