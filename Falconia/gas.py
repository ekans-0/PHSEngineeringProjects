import RPi.GPIO as GPIO
import csv
import time

# Set GPIO mode (BCM or BOARD)
GPIO.setmode(GPIO.BCM)  # BCM mode is typically used for Raspberry Pi

# Set up GPIO for Gas sensor
GAS_SENSOR_PIN = 26
GPIO.setup(GAS_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# CSV file path
csv_file = 'gas_sensor_data.csv'

# Check if the CSV file exists and write headers if necessary
try:
    with open(csv_file, mode='x', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Timestamp', 'Gas Detected'])
except FileExistsError:
    # If the file already exists, don't write headers again
    pass

def read_gas_sensor():
    # Read the gas sensor
    if GPIO.input(GAS_SENSOR_PIN) == GPIO.HIGH:
        status = "No gas detected"
        print(status)
    else:
        status = "Gas detected!"
        print(status)

    # Get the timestamp
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

    # Write data to the CSV file (append mode)
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, status])

# Run the function once
read_gas_sensor()

# Clean up GPIO setup
GPIO.cleanup()
