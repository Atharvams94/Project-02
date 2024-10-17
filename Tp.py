import numpy as np

class WeatherFetcher:
    def __init__(self, api_key, base_url="http://api.openweathermap.org/data/2.5/weather"):
        self.api_key = api_key
        self.base_url = base_url

    async def get_and_save_weather(self, city):
        try:
            data = await self.fetch_weather(city)
            weather_report = self.parse_weather_data(data)
            print(f"Weather in {city}:\n{weather_report}")
            await self.save_weather_data(city, data)
        except Exception as e:
            print(f"Error fetching weather data for {city}: {e}")



