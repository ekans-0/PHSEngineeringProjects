import time
import curses
import board
import busio
from adafruit_motorkit import MotorKit

# Initialize the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize the MotorKit object with I2C bus
kit = MotorKit(i2c=i2c)

# Function to stop motors
def stop_motors():
    kit.motor1.throttle = 0
    kit.motor4.throttle = 0

# Function to move forward
def move_forward():
    kit.motor1.throttle = 0.75
    kit.motor4.throttle = 0.75

# Function to move backward
def move_backward():
    kit.motor1.throttle = -0.75
    kit.motor4.throttle = -0.75

# Function to turn left
def turn_left():
    kit.motor1.throttle = 0
    kit.motor4.throttle = 1

# Function to turn right
def turn_right():
    kit.motor1.throttle = 1
    kit.motor4.throttle = 0

# Function to move diagonally forward-left
def move_diagonal_forward_left():
    kit.motor1.throttle = 0.1
    kit.motor4.throttle = 0.75

# Function to move diagonally forward-right
def move_diagonal_forward_right():
    kit.motor1.throttle = 0.75
    kit.motor4.throttle = 0.1

# Function to move diagonally backward-left
def move_diagonal_backward_left():
    kit.motor1.throttle = -0.1
    kit.motor4.throttle = -0.75

# Function to move diagonally backward-right
def move_diagonal_backward_right():
    kit.motor1.throttle = -0.75
    kit.motor4.throttle = -0.1

# Function to spin left
def spin_left():
    kit.motor1.throttle = -0.75
    kit.motor4.throttle = 0.75

# Function to spin right
def spin_right():
    kit.motor1.throttle = 0.75
    kit.motor4.throttle = -0.75

def main(stdscr):
    # Set up curses
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)   # Non-blocking input
    stdscr.timeout(100)  # Refresh timeout

    stdscr.addstr(0, 0, "Use WASD for movement, QEZX for diagonals, JL for spin turns:")
    stdscr.refresh()

    try:
        while True:
            key = stdscr.getch()

            if key == ord('w'):  # Forward
                stdscr.clear()
                stdscr.addstr(0, 0, "Moving forward")
                move_forward()

            elif key == ord('s'):  # Backward
                stdscr.clear()
                stdscr.addstr(0, 0, "Moving backward")
                move_backward()

            elif key == ord('a'):  # Left
                stdscr.clear()
                stdscr.addstr(0, 0, "Turning left")
                turn_left()

            elif key == ord('d'):  # Right
                stdscr.clear()
                stdscr.addstr(0, 0, "Turning right")
                turn_right()

            elif key == ord('q'):  # Diagonal forward-left
                stdscr.clear()
                stdscr.addstr(0, 0, "Moving diagonally forward-left")
                move_diagonal_forward_left()

            elif key == ord('e'):  # Diagonal forward-right
                stdscr.clear()
                stdscr.addstr(0, 0, "Moving diagonally forward-right")
                move_diagonal_forward_right()

            elif key == ord('z'):  # Diagonal backward-left
                stdscr.clear()
                stdscr.addstr(0, 0, "Moving diagonally backward-left")
                move_diagonal_backward_left()

            elif key == ord('c'):  # Diagonal backward-right
                stdscr.clear()
                stdscr.addstr(0, 0, "Moving diagonally backward-right")
                move_diagonal_backward_right()

            elif key == ord('j'):  # Spin left
                stdscr.clear()
                stdscr.addstr(0, 0, "Spinning left")
                spin_left()

            elif key == ord('l'):  # Spin right
                stdscr.clear()
                stdscr.addstr(0, 0, "Spinning right")
                spin_right()

            else:  # If no key is pressed, stop motors
                stop_motors()
                stdscr.clear()
                stdscr.addstr(0, 0, "Motors stopped")

            stdscr.refresh()

    except KeyboardInterrupt:
        stop_motors()
        print("\nExiting...")

if __name__ == "__main__":
    curses.wrapper(main)
