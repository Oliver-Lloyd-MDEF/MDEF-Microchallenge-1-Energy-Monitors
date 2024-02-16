import sys
import os
from PyP100 import PyP110
import time
import requests
import asyncio
import websockets

Sendvalue = None

p110 = PyP110.P110("172.16.20.64", "carlottahylkema@gmail.com", "IAACMDEF24!")

# Define a mapping of keywords to the words you want to append
word_mapping = {
    "runtime": "minutes",
    "energy": "watts",
    "power": "watts",
}

async def handle_connection(websocket, path):
    # This function will be called each time a new connection is established
    print("Client connected")
    try:
        while True:
            energy = p110.getEnergyUsage()  # Returns dict with all of the energy usage of the connected plug
            
            # Extract required values
            today_energy = energy.get("today_energy", 0)
            month_energy = energy.get("month_energy", 0)
            today_runtime = energy.get("today_runtime", 0)
            month_runtime = energy.get("month_runtime", 0)

            print (today_energy)
            print(month_energy)

            Sendvalue = today_energy
            # Send the value to the connected client
            print("Sending value:", (Sendvalue))
            await websocket.send(str(Sendvalue))
            
            # Wait for 5 seconds before sending the next value
            await asyncio.sleep(5)
                                                                              
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")  
        
        # Wait for 5 seconds before the next reading
        await asyncio.sleep(5)

# Function to run the WebSocket server
async def run_websocket_server():
    # Start the WebSocket server
    async with websockets.serve(handle_connection, 'localhost', 8080):
        print("WebSocket server started")
        # Run the event loop
        await asyncio.Future()  # Run indefinitely

# Run the WebSocket server
asyncio.run(run_websocket_server())
