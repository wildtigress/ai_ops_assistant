import os
from dotenv import load_dotenv

load_dotenv()

print("GROQ_API_KEY =", os.getenv("GROQ_API_KEY"))
print("WEATHER_API_KEY =", os.getenv("WEATHER_API_KEY"))
