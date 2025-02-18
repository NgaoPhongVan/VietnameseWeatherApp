# config.py
import os
from dotenv import load_dotenv

load_dotenv()

# OpenWeatherMap config
OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')
WEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

# API Ninjas config
NINJAS_API_KEY = os.getenv('NINJAS_API_KEY')
NINJAS_BASE_URL = "https://api.api-ninjas.com/v1/geocoding"