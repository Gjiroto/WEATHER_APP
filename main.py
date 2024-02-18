from api import get_weather, get_forecast
from weather import show_current_weather, show_forecast
from config import API_KEY

def main():
    while True:
        city = input("Enter city name: ")
        api_key = API_KEY
        weather_data = get_weather(city, api_key)
        if weather_data["cod"] == 200:
            show_current_weather(weather_data)
        else:
            print("City not found. Please try again.")
            continue

        forecast_data = get_forecast(city, api_key)
        if forecast_data["cod"] == "200":
            show_forecast(forecast_data)
        else:
            print("City not found. Please try again.")
            continue

        option = input("Do you want to search for weather in another city? (y/n): ")
        if option.lower() != 'y':
            break

if __name__ == "__main__":
    main()
