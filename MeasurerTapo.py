import sys
import os 
import msvcrt
from PyP100 import PyP110
import time

# Function to check if there's input available on stdin
def is_input_available():
    return msvcrt.kbhit()

p110 = PyP110.P110("172.16.20.64", "carlottahylkema@gmail.com", "IAACMDEF24!")

# Define a mapping of keywords to the words you want to append
word_mapping = {
    "runtime": "minutes",
    "energy": "watts",
    "power": "watts",
}

while True:
    # The P110 has all the same basic functions as the plugs and additionally allow for energy monitoring.
    energy = p110.getEnergyUsage()  # Returns dict with all of the energy usage of the connected plug


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
            
    # Check for user input to stop the script
    if is_input_available():
        user_input = input().strip().lower()
        if user_input == 'stop':
            print("Exiting...")
            break
            
    # Wait for 30 seconds before the next reading
    time.sleep(5)