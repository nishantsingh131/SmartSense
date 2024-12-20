import serial
import time
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import json

# Initialize Flask app and SocketIO
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")  # Allow cross-origin requests

# Serial port configuration
arduino_port = "COM6"  # Update this to your actual COM port
baud_rate = 9600

try:
    ser = serial.Serial(arduino_port, baud_rate, timeout=2)  # Increased timeout
    ser.flushInput()  # Clear serial buffer
    print(f"Connected to Arduino on port {arduino_port}")
except Exception as e:
    ser = None
    print(f"Error connecting to Arduino: {e}")

# Function to parse sensor data
def parse_sensor_data(line):
    try:
        data = json.loads(line)  # Parse JSON data
        return {
            "temperature": data.get("temperature"),
            "humidity": data.get("humidity"),
            "mq_value": data.get("mq_value"),
            "time": data.get("time")
        }
    except json.JSONDecodeError as e:
        print(f"JSON parse error: {e} | Raw line: {line}")
        return None

# Function to read data from Arduino
def read_arduino_data():
    if not ser:
        print("Serial connection is not established.")
        return

    while True:
        try:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').strip()
                print(f"Raw data received: {line}")
                parsed_data = parse_sensor_data(line)
                if parsed_data:
                    print(f"Emitting data: {parsed_data}")
                    socketio.emit('sensor_data', parsed_data)
            else:
                print("No data available on serial port.")
            time.sleep(1)  # Avoid CPU overutilization
        except Exception as e:
            print(f"Error reading serial data: {e}")

# Route for the index page
@app.route('/')
def index():
    return render_template('index.html')

# Handle LED control from frontend
@socketio.on('control_led')
def handle_led_control(data):
    try:
        command = data.get('command')  # ON or OFF
        if command == "ON":
            ser.write(b'ON\n')  # Send ON command to Arduino
            print("LED ON command sent")
        elif command == "OFF":
            ser.write(b'OFF\n')  # Send OFF command to Arduino
            print("LED OFF command sent")
        emit('led_status', {'status': command})  # Acknowledge frontend
    except Exception as e:
        print(f"Error controlling LED: {e}")

if __name__ == "__main__":
    # Start reading Arduino data in a background thread
    if ser:
        socketio.start_background_task(target=read_arduino_data)
    socketio.run(app, host='0.0.0.0', port=5000)
