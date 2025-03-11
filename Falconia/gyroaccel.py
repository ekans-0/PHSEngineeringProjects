# gyroaccel.py
import smbus2

# MPU6050 I2C address and register setup
MPU6050_ADDRESS = 0x68
bus = smbus2.SMBus(1)

# Initialize the MPU6050
def initialize_gyroaccel():
    bus.write_byte_data(MPU6050_ADDRESS, 0x6B, 0)  # Wake up the MPU6050

def read_gyroaccel():
    def read_word(register):
        high = bus.read_byte_data(MPU6050_ADDRESS, register)
        low = bus.read_byte_data(MPU6050_ADDRESS, register + 1)
        value = (high << 8) + low
        if value >= 0x8000:
            value -= 0x10000
        return value

    # Read accelerometer and gyroscope data
    accel_x = read_word(0x3B)
    accel_y = read_word(0x3D)
    accel_z = read_word(0x3F)
    gyro_x = read_word(0x43)
    gyro_y = read_word(0x45)
    gyro_z = read_word(0x47)

    # Print the data
    print(f"Accelerometer -> X: {accel_x}, Y: {accel_y}, Z: {accel_z}")
    print(f"Gyroscope -> X: {gyro_x}, Y: {gyro_y}, Z: {gyro_z}")

# Call this function to initialize the MPU6050 sensor
initialize_gyroaccel()
