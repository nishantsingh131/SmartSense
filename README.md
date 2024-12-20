# Sensor Monitoring System

This project integrates various sensors (RTC, MQ 135, DHT11) with an OLED display and a buzzer. It is managed through a Python server, and the sensor data is displayed on a frontend built using HTML, CSS, and JavaScript. The system monitors environmental parameters such as air quality, temperature, and humidity, providing real-time data on the web interface.

## Components

- **RTC (Real-Time Clock)**: Keeps track of the current date and time.
- **MQ 135**: Air quality sensor for detecting gases like CO2, ammonia, and other pollutants.
- **DHT11**: Temperature and humidity sensor.
- **OLED Display**: A 0.96-inch OLED screen to display sensor data.
- **Buzzer**: Provides alerts based on specific sensor readings (e.g., air quality or temperature thresholds).
- **Python Server**: Handles the backend logic and communicates with the sensors.
- **Frontend (HTML, CSS, JavaScript)**: Displays the sensor data in real-time.

## Features

- Real-time monitoring of air quality, temperature, and humidity.
- Data is displayed on an OLED screen.
- Alerts are generated through a buzzer if certain sensor thresholds are exceeded.
- Web interface to view live data from the sensors.
- The system is powered by a Python server that communicates with the hardware and serves data to the frontend.

## Requirements

### Hardware

- **ESP32** or any Arduino Uno Board
- **MQ 135 Sensor**
- **DHT11 Sensor**
- **RTC Module**
- **0.96-inch OLED Display**
- **Buzzer**
- Jumper wires and breadboard for connections.

### Software

- Python 3.x
- Flask (or another Python web framework for the server)
- HTML, CSS, and JavaScript for frontend development
- Any necessary libraries for interfacing with sensors (e.g., `Adafruit_DHT`, `time`, etc.)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
