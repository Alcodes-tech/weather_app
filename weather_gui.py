import requests
import tkinter as tk
import datetime
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather():
    city = city_entry.get()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather = data['weather'][0]['description'].capitalize()
        temp = data['main']['temp']

        timezone_offset = data.get('timezone', 0)  # seconds offset from UTC
        utc_now = datetime.datetime.utcnow()
        local_time = utc_now + datetime.timedelta(seconds=timezone_offset)
        formatted_time = local_time.strftime('%Y-%m-%d %H:%M:%S')

        result_label.config(text=f"{city} - {weather}\n{temp}°C\nLocal time: {formatted_time}")
    else:
        result_label.config(text="City not found or error!")

def center_window(win, width, height):
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    win.geometry(f"{width}x{height}+{x}+{y}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("🌤️ Weather App")
    root.configure(bg="#282c34")
    center_window(root, 400, 250)

    frame = tk.Frame(root, bg="#282c34")
    frame.pack(pady=20, padx=20)

    city_entry = tk.Entry(frame, font=('Helvetica', 14), bg="#3c4048", fg="white", insertbackground="white")
    city_entry.pack(side="left", padx=(0,10))
    city_entry.bind("<Return>", lambda event: get_weather())  # Bind Enter key

    result_label = tk.Label(root, text="", font=('Helvetica', 16), bg="#282c34", fg="white")
    result_label.pack(pady=20)

    root.mainloop()

