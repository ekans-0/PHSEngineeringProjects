import RPi.GPIO as GPIO
import csv
import time

# Set up GPIO for Hall sensor
HALL_SENSOR_PIN = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(HALL_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# CSV file path
csv_file = 'Data/hall_sensor_data.csv'

# Check if the CSV file exists and write headers if necessary
try:
    with open(csv_file, mode='x', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Timestamp', 'Magnetic Field Detected'])
except FileExistsError:
    # If the file already exists, don't write headers again
    pass

def read_hall_sensor():
    # Read the Hall sensor
    if GPIO.input(HALL_SENSOR_PIN) == GPIO.HIGH:
        status = "No magnetic field detected"
        print(status)
    else:
        status = "Magnetic field detected"
        print(status)

    # Get the timestamp
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

    # Write data to the CSV file (append mode)
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, status])

# Run the function once
read_hall_sensor()

# Clean up GPIO setup
GPIO.cleanup()
