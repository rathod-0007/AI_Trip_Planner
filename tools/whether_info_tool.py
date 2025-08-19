import os
import requests
from utils.weather_info import WeatherForecastTool
from langchain.tools import tool
from typing import List
from dotenv import load_dotenv

class WeatherInfoTool:
    def __init__(self):
        load_dotenv()
        self.api_key = os.environ.get("OPENWEATHERMAP_API_KEY")
        self.weather_service = WeatherForecastTool(self.api_key)
        self.backend_url = os.environ.get("BACKEND_URL", "http://localhost:8000/query")
        self.weather_tool_list = self._setup_tools()
    
    def _setup_tools(self) -> List:
        """Setup all tools for the weather forecast tool"""

        @tool
        def get_current_weather(city: str) -> str:
            """Get current weather for a city"""
            try:
                weather_data = self.weather_service.get_current_weather(city)
                if weather_data:
                    temp = weather_data.get('main', {}).get('temp', 'N/A')
                    desc = weather_data.get('weather', [{}])[0].get('description', 'N/A')
                    return f"Current weather in {city}: {temp}°C, {desc}"
                return f"Could not fetch weather for {city}"
            except Exception as e:
                return f"Error fetching current weather: {str(e)}"
        
        @tool
        def get_weather_forecast(city: str) -> str:
            """Get weather forecast for a city"""
            try:
                forecast_data = self.weather_service.get_forecast_weather(city)
                if forecast_data and 'list' in forecast_data:
                    forecast_summary = []
                    for item in forecast_data['list']:
                        date = item['dt_txt'].split(' ')[0]
                        temp = item['main']['temp']
                        desc = item['weather'][0]['description']
                        forecast_summary.append(f"{date}: {temp}°C, {desc}")
                    return f"Weather forecast for {city}:\n" + "\n".join(forecast_summary)
                return f"Could not fetch forecast for {city}"
            except Exception as e:
                return f"Error fetching forecast: {str(e)}"

        return [get_current_weather, get_weather_forecast]
