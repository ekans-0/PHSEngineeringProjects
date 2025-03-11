import RPi.GPIO as GPIO

# Set up GPIO for Hall sensor
HALL_SENSOR_PIN = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(HALL_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def read_hall_sensor():
    if GPIO.input(HALL_SENSOR_PIN) == GPIO.HIGH:
        print("No magnetic field detected.")
    else:
        print("Magnetic field detected.")
