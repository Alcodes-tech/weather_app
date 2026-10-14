# weather_app.py
import requests # type: ignore

API_KEY = '87343eb80377dc5af0a1dcd6fd66d136'  # Replace with your OpenWeatherMap API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        print(f"\nWeather in {data['name']}, {data['sys']['country']}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Feels like: {data['main']['feels_like']}°C")
        print(f"Weather: {data['weather'][0]['description'].capitalize()}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind speed: {data['wind']['speed']} m/s")
    else:
        print("\n❌ City not found or error in API request.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
