import RPi.GPIO as GPIO
import csv
import time
import os

# Hall sensor GPIO pin (change if needed)
HALL_SENSOR_PIN = 12

# Ensure GPIO mode is set (only if not already set)
if GPIO.getmode() is None:
    GPIO.setmode(GPIO.BCM)

# Set up GPIO for Hall sensor
GPIO.setup(HALL_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Ensure the Data directory exists
if not os.path.exists("Data"):
    os.makedirs("Data")

# CSV file path
csv_file = 'Data/hall_sensor_data.csv'

# Create CSV file with headers if it doesn't exist
if not os.path.exists(csv_file):
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Timestamp', 'Magnetic Field Detected'])

def read_hall_sensor():
    """Read Hall sensor data and write it to the CSV file."""
    # Read the Hall sensor
    if GPIO.input(HALL_SENSOR_PIN) == GPIO.HIGH:
        status = "No magnetic field detected"
    else:
        status = "Magnetic field detected"
    
    # Get the timestamp
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    
    # Write data to CSV (append mode)
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, status])
    
    # Print the status to the terminal
    print(f"{timestamp} - {status}")

# Only run this block if the module is executed directly
if __name__ == '__main__':
    read_hall_sensor()
    GPIO.cleanup()
