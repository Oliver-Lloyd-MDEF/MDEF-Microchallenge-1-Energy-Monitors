import sys
import os
from PyP100 import PyP110
import time
import requests


p110 = PyP110.P110("172.16.20.64", "carlottahylkema@gmail.com", "IAACMDEF24!")

# Function to send data to Node-RED dashboard
def send_to_nodered_dashboard(data):
    try:
        url = "http://172.16.22.127:1880/data"  # Replace with your Node-RED endpoint
        response = requests.post(url, json={"value": data}, timeout=30)  # 10 seconds timeout
        if response.status_code == 200:
            print("Data sent to Node-RED dashboard successfully.")
        else:
            print(f"Failed to send data to Node-RED dashboard. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending data to Node-RED dashboard: {e}", sys.exc_info())

# Define a mapping of keywords to the words you want to append
word_mapping = {
    "runtime": "minutes",
    "energy": "watts",
    "power": "watts",
}


while True:  # Run the loop as long as running is True
    energy = p110.getEnergyUsage()  # Returns dict with all of the energy usage of the connected plug

    # Extract required values
    today_energy = energy.get("today_energy", 0)
    month_energy = energy.get("month_energy", 0)
    today_runtime = energy.get("today_runtime", 0)
    month_runtime = energy.get("month_runtime", 0)

    # Prepare data payload
    data = {
        "today_energy": today_energy,
        "month_energy": month_energy,
        "today_runtime": today_runtime,
        "month_runtime": month_runtime
    }

    print(data)

    # Iterate over the dictionary keys and print the values with appended words
    for key, value in energy.items():
        for keyword, word in word_mapping.items():
            if keyword in key.lower():
                if keyword == "power":
                    value /= 1000  # Convert power from units of 37000 to 37
                print(f"{key}: {value} {word}")
                break
        else:
            print(f"{key}: {value}")

    # Send data to Node-RED dashboard
    send_to_nodered_dashboard(data)
            
    # Wait for 5 seconds before the next reading
    time.sleep(5)