# Weather App

This program allows users to check the current weather and 5-day forecast for a specific city. It uses the OpenWeatherMap API to retrieve weather data.

## How to Run

1. Clone the repository to your local machine.
2. Install the required dependencies by running:

    ```
    pip install -r requirements.txt
    ```

3. Create a file named `config.py` in the root directory of the project and add your OpenWeatherMap API key as follows:
    ...
    repr
    API_KEY = "your_api_key"
    ```

4. Run the program using the following command:

    ```
    python3 main.py
    ```

5. Enter the city name in the format "City, CountryCode" (e.g., "New York, US") when prompted.

Enter city name: New York, US
Current weather: 4.31°C - clear sky

Date               Temperature     Description
------------------- --------------- -------------------
2024-02-18 21:00:00 4.29°C          clear sky
2024-02-19 00:00:00 3.46°C          clear sky
2024-02-19 03:00:00 2.46°C          clear sky
2024-02-19 06:00:00 0.63°C          few clouds
2024-02-19 09:00:00 -0.01°C         clear sky
2024-02-19 12:00:00 -0.38°C         clear sky
2024-02-19 15:00:00 0.62°C          clear sky
2024-02-19 18:00:00 2.71°C          clear sky
2024-02-19 21:00:00 3.8°C           clear sky
2024-02-20 00:00:00 2.38°C          clear sky
2024-02-20 03:00:00 0.48°C          clear sky
2024-02-20 06:00:00 -0.42°C         clear sky

Note: Replace `"your_api_key"` in `config.py` with your actual OpenWeatherMap API key.
