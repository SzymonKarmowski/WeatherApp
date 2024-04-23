import tkinter as tk
from tkinter import ttk
import requests
from datetime import datetime

API_KEY = "fe2daf392dd5fe699bcee9361c90ee8c"


def kelvin_to_celsius(k):
    return round(k - 273.15, 2)


def timestamp_to_time(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime('%H:%M:%S')


def get_weather():

    city_name = city_entry.get()

    coordinates_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={1}&appid={API_KEY}"

    coordinates_response = requests.get(coordinates_url).json()
    coord_lat = coordinates_response[0]['lat']
    coord_lon = coordinates_response[0]['lon']

    current_weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={coord_lat}&lon={coord_lon}&appid={API_KEY}"

    response = requests.get(current_weather_url).json()

    weather_info_label.config(text=f"Weather Information for {response['name']}")
    description_label.config(text=f"{response['weather'][0]['description'].title()}")
    temperature_label.config(text=f"{kelvin_to_celsius(response['main']['temp'])}°C")
    feels_like_label.config(text=f"Feels Like: {kelvin_to_celsius(response['main']['feels_like'])}°C")
    min_temp_label.config(text=f"Min Temperature: {kelvin_to_celsius(response['main']['temp_min'])}°C")
    max_temp_label.config(text=f"Max Temperature: {kelvin_to_celsius(response['main']['temp_max'])}°C")
    pressure_label.config(text=f"Pressure: {response['main']['pressure']} hPa")
    humidity_label.config(text=f"Humidity: {response['main']['humidity']}%")
    wind_speed_label.config(text=f"Wind Speed: {response['wind']['speed']} m/s")
    wind_direction_label.config(text=f"Wind Direction: {response['wind']['deg']}°")
    cloudiness_label.config(text=f"Cloudiness: {response['clouds']['all']}%")
    visibility_label.config(text=f"Visibility: {response['visibility']} m")
    sunrise_label.config(text=f"Sunrise Time: {timestamp_to_time(response['sys']['sunrise'])}")
    sunset_label.config(text=f"Sunset Time: {timestamp_to_time(response['sys']['sunset'])}")


root = tk.Tk()
root.title("Weather Information")
root.geometry("310x450")

city_label = ttk.Label(root, text="Enter city name:")
city_label.grid(row=0, column=0, padx=10, pady=10)
city_entry = ttk.Entry(root, width=30)
city_entry.grid(row=0, column=1, padx=10, pady=10)
city_entry.focus()


get_weather_button = ttk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.grid(row=1, column=0, columnspan=2, pady=10)


weather_info_label = ttk.Label(root, font=("Helvetica", 14, "bold"))
weather_info_label.grid(row=2, column=0, columnspan=2, pady=10)

description_label = ttk.Label(root, font=("Helvetica", 12))
description_label.grid(row=3, column=0, columnspan=2)

temperature_label = ttk.Label(root, font=("Helvetica", 16, "bold"))
temperature_label.grid(row=4, column=0, columnspan=2)

feels_like_label = ttk.Label(root)
feels_like_label.grid(row=5, column=0, columnspan=2)

min_temp_label = ttk.Label(root)
min_temp_label.grid(row=6, column=0, columnspan=2)

max_temp_label = ttk.Label(root)
max_temp_label.grid(row=7, column=0, columnspan=2)

pressure_label = ttk.Label(root)
pressure_label.grid(row=8, column=0, columnspan=2)

humidity_label = ttk.Label(root)
humidity_label.grid(row=9, column=0, columnspan=2)

wind_speed_label = ttk.Label(root)
wind_speed_label.grid(row=10, column=0, columnspan=2)

wind_direction_label = ttk.Label(root)
wind_direction_label.grid(row=11, column=0, columnspan=2)

cloudiness_label = ttk.Label(root)
cloudiness_label.grid(row=12, column=0, columnspan=2)

visibility_label = ttk.Label(root)
visibility_label.grid(row=13, column=0, columnspan=2)

sunrise_label = ttk.Label(root)
sunrise_label.grid(row=14, column=0, columnspan=2)

sunset_label = ttk.Label(root)
sunset_label.grid(row=15, column=0, columnspan=2)

root.mainloop()
