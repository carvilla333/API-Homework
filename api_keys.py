from dotenv import load_dotenv
import os
load_dotenv()

# OpenWeatherMap API Key
weather_api_key = os.getenv("weather_api_key")

# Google API Key
g_key = os.getenv("g_key")
