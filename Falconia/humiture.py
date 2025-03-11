import adafruit_dht
import board
import csv
import time

# Set up DHT11 sensor
DHT_SENSOR = adafruit_dht.DHT11(board.D17)

# CSV file path
csv_file = 'humiture_data.csv'

# Check if the CSV file exists and write headers if necessary
try:
    with open(csv_file, mode='x', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Timestamp', 'Temperature (°C)', 'Humidity (%)'])
except FileExistsError:
    # If the file already exists, don't write headers again
    pass

def read_humiture():
    try:
        # Read data from the sensor
        temperature = DHT_SENSOR.temperature
        humidity = DHT_SENSOR.humidity
        
        # Check if values are valid
        if temperature is not None and humidity is not None:
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
            print(f"Timestamp: {timestamp}")
            print(f"Temperature: {temperature:.1f} °C")
            print(f"Humidity: {humidity:.1f} %")
            
            # Write data to the CSV file (append mode)
            with open(csv_file, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([timestamp, temperature, humidity])
        else:
            print("Error: Unable to read from Humiture sensor.")
    except RuntimeError as e:
        print(f"Runtime error reading Humiture sensor: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Run the function once
read_humiture()
