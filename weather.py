from tabulate import tabulate
from colorama import Fore, Style

def show_current_weather(weather_data):
    current_weather = weather_data["main"]["temp"]
    weather_description = weather_data["weather"][0]["description"]
    print(Fore.BLUE + f"Current weather: {current_weather}°C - {weather_description}" + Fore.RESET + "\n")

def show_forecast(weather_forecast):
    forecast_info = []
    for forecast in weather_forecast["list"]:
        date = forecast["dt_txt"]
        temperature = forecast["main"]["temp"]
        description = forecast["weather"][0]["description"]
        forecast_info.append([date, f"{temperature}°C", description])

    table = tabulate(forecast_info, headers=["Date", "Temperature", "Description"], tablefmt="fancy_grid")
    print(Fore.GREEN + table + Fore.RESET + "\n")
