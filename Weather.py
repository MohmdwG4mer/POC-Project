import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key

def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description'].capitalize()
        result_label.config(text=f"{city.capitalize()}:\n{temp}°C, {desc}")
    else:
        result_label.config(text="City not found or API error.")

# ---------------- GUI Setup ----------------

root = tk.Tk()
root.title("Weather App")
root.geometry("300x200")
root.resizable(False, False)

title_label = tk.Label(root, text="Enter City Name", font=("Helvetica", 14))
title_label.pack(pady=10)

city_entry = tk.Entry(root, width=30)
city_entry.pack()

search_button = tk.Button(root, text="Get Weather", command=get_weather)
search_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

root.mainloop()