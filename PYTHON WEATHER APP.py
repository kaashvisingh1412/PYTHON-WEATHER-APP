# basic_weather_app_no_requests.py

import time
import random

print("====================================")
print("       Welcome to Weather App       ")
print("   (Simulated Data Version)         ")
print("====================================\n")

# Simulated weather database
weather_data = {
    "London": {"temp": 18, "humidity": 72, "condition": "Clear sky"},
    "Paris": {"temp": 22, "humidity": 65, "condition": "Partly cloudy"},
    "New York": {"temp": 25, "humidity": 70, "condition": "Sunny"},
    "Tokyo": {"temp": 28, "humidity": 75, "condition": "Rainy"},
    "Delhi": {"temp": 35, "humidity": 40, "condition": "Hot"}
}

while True:
    city = input("Enter the name of the city (or type 'exit' to quit): ").strip()
    
    if city.lower() == "exit":
        print("\nThank you for using Weather App!")
        break

    if city == "":
        print("City name cannot be empty. Please try again.\n")
        continue

    print("\nFetching weather data for", city, "...")
    time.sleep(1)  # simulate delay

    if city in weather_data:
        data = weather_data[city]
        # Add slight random variation to make it look dynamic
        temp = data["temp"] + random.randint(-2, 2)
        humidity = data["humidity"] + random.randint(-5, 5)
        condition = data["condition"]

        print("\n========== Weather Report ==========")
        print(f"City: {city}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {condition}")
        print("===================================\n")
    else:
        print("City not found in database. Try London, Paris, New York, Tokyo, or Delhi.\n")

    time.sleep(1)
    print("You can check another city or type 'exit' to quit.\n")
