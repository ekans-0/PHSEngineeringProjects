import adafruit_dht
import board

# Set up DHT11 sensor
DHT_SENSOR = adafruit_dht.DHT11(board.D17)

def read_humiture():
    try:
        temperature = DHT_SENSOR.temperature
        humidity = DHT_SENSOR.humidity
        if temperature is not None and humidity is not None:
            print(f"Temperature: {temperature:.1f} °C")
            print(f"Humidity: {humidity:.1f} %")
        else:
            print("Error: Unable to read from Humiture sensor.")
    except RuntimeError as e:
        print(f"Runtime error reading Humiture sensor: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
