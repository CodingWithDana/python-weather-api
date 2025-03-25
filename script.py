""" 
This script returns the current weather in the specified location.

Setup:
    * Sign up for a free account at https://www.weatherapi.com
    * Get the API key from the dashboard
    * Set the API key as an environment variable in your terminal called WEATHER_API_KEY
        e.g. export WEATHER_API_KEY=<your_api_key>

Usage:
    python script.py <name> <location>
    e.g. python script.py Dana Melbourne
"""

import sys
import os
import requests

# Error Handling - Argument Validation
if len(sys.argv) != 3:
    print("Error: Invalid number of arguments")
    print("Usage: python script.py <name> <location>")
    sys.exit()

# Command Line Arguments
name = sys.argv[1]
location = sys.argv[2]

# Get the API KEY value from ENVIRONMENT VARIABLES
api_key = os.environ.get('WEATHER_API_KEY')

try:
    # Constructing the API REQUEST URL 
    url = 'https://api.weatherapi.com/v1/current.json?key=' + api_key + '&q=' + location + '&aqi=yes'

    # Making the API REQUEST (a.k.a API Call)
    response = requests.get(url)

    # Converting the Response to JSON
    response = response.json()

    # Get weather data
    temperature = response['current']['temp_c']
    condition = response['current']['condition']['text']

    # Console Output
    print("Hi" + " " + name)
    print("\nHere's the weather in " + location + ":")
    print("Temperature: " + str(temperature) + "°C")
    print("Condition: " + condition)
except:
    print("Error: Failed to make API call successfully")
    sys.exit()