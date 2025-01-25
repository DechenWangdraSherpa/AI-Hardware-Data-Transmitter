# Data-Transmitter

This script processes data received from the sensors, formats it into JSON, and transmits the processed data to a backend server. For now, the data originates from a dummy WebSocket server.

---

## **Features**
- Receives data from sensors.
- Parses the received data into JSON format.
- Sends the parsed data to a specified backend endpoint.

---

## **Requirements**

### **Dependencies**
Install the following Python libraries:

```bash
pip install websocket-client requests
```

### **Backend Endpoint**
Ensure you have a backend server running and replace the `backend_url` variable in the code with the correct endpoint URL (e.g., `http://localhost:3001/api/receive-data`).

---

## **Setup Instructions**

1. Clone the repository or copy the script to your local machine.
2. Install the required dependencies using:
   ```bash
   pip install websocket-client requests
   ```
3. Ensure the backend server is running and accessible.
4. Start the dummy WebSocket server (replace with your real server when available). 
   - Example dummy server URL: `ws://127.0.0.1:8765`

---

## **Running the Application**

1. Open a terminal in the directory where the script is located.
2. Run the script:
   ```bash
   python script_name.py
   ```
   Replace `script_name.py` with the filename of the script.
3. Ensure the backend and dummy server are running simultaneously.

---

## **What the Code Does**
- Connects to a WebSocket server (default: `ws://127.0.0.1:8765`).
- Processes data received from the server (currently coming from a dummy server).
- Transmits the processed data to the backend API endpoint (`backend_url`).
- Logs success or error messages to the console.

---

## **Customization**
- Replace `dummy_server_url` with the actual WebSocket server URL when available.
- Update `backend_url` to match your backend endpoint.

---

## **Note**
This project currently uses a dummy server to simulate data. Replace it with your actual data source when integrating with real sensors or hardware.

