import websocket
import requests
import json

# URL of the backend endpoint to send data
backend_url = "http://localhost:3001/api/receive-data"  # Replace with your backend URL
# https://ai-backend-server.onrender.com/api/receive-data
# http://localhost:3001/api/receive-data

# WebSocket server address
dummy_server_url = "ws://127.0.0.1:8765"  # Replace with the actual WebSocket server URL

def on_message(ws, message):
    try:
        # Parse the message received from the WebSocket server
        parsed_data = json.loads(message)

        # Send the parsed data to the backend
        response = requests.post(backend_url, json=parsed_data)
        
        # Check the response from the backend
        if response.status_code == 200:
            print("Data successfully sent to backend")
        else:
            print(f"Failed to send data to backend: {response.status_code}")

    except Exception as e:
        print(f"Error handling message: {e}")

def on_error(ws, error):
    print(f"WebSocket error: {error}")

def on_close(ws, close_status_code, close_msg):
    print("WebSocket connection closed")

def on_open(ws):
    print("Connected to WebSocket server")

# Establish WebSocket connection
ws = websocket.WebSocketApp(dummy_server_url,
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close)

# Start WebSocket connection
ws.on_open = on_open
ws.run_forever()
