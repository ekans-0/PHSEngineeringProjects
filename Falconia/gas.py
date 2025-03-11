# gas.py
import RPi.GPIO as GPIO

# Set up GPIO for Gas sensor
GAS_SENSOR_PIN = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(GAS_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def read_gas_sensor():
    if GPIO.input(GAS_SENSOR_PIN) == GPIO.HIGH:
        print("No gas detected.")
    else:
        print("Gas detected!")
