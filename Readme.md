# Weather App

This program allows users to check the current weather and 5-day forecast for a specific city. It uses the OpenWeatherMap API to retrieve weather data.

## How to Run

1. Clone the repository to your local machine.
2. Install the required dependencies by running:

    ```
    pip install -r requirements.txt
    ```

3. Create a file named `config.py` in the root directory of the project and add your OpenWeatherMap API key as follows:
   
    ```python
    API_KEY = "your_api_key"
    ```

5. Run the program using the following command:

    ```
    python3 main.py
    ```

6. Enter the city name in the format "City, CountryCode" (e.g., "New York, US") when prompted.

Enter city name: New York, US
Current weather: 4.31°C - clear sky

Note: Replace `"your_api_key"` in `config.py` with your actual OpenWeatherMap API key.
