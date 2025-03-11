import time
import curses
import signal
import sys
import humiture
import electro
import gas
import gyroaccel  # Import the new gyroaccel module

# Gracefully exit on SIGINT (Ctrl+C)
def signal_handler(sig, frame):
    print("Exiting gracefully...")
    GPIO.cleanup()  # Ensure GPIO pins are cleaned up properly
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Main Function with Curses UI
def main(stdscr):
    stdscr.clear()
    stdscr.nodelay(1)  # Non-blocking input mode

    # Instructions
    stdscr.addstr(0, 0, "Press 'h' for Humiture test (DHT sensor)")
    stdscr.addstr(1, 0, "Press 'e' for Hall sensor test")
    stdscr.addstr(2, 0, "Press 'g' for Gas sensor test")
    stdscr.addstr(3, 0, "Press 'a' for Gyroscope/Accelerometer test")
    stdscr.addstr(4, 0, "Press 'q' to quit")
    stdscr.refresh()

    while True:
        key = stdscr.getch()

        if key == ord('h'):
            stdscr.clear()
            stdscr.addstr(0, 0, "Running Humiture test (DHT sensor) for 15 seconds...")
            stdscr.refresh()

            start_time = time.time()
            while time.time() - start_time < 15:  # Run for 15 seconds
                humiture.read_humiture()  # Run Humiture sensor
                time.sleep(1)  # Wait for 1 second between readings (to avoid overwhelming the terminal)

        elif key == ord('e'):
            stdscr.clear()
            stdscr.addstr(0, 0, "Running Hall sensor test for 15 seconds...")
            stdscr.refresh()

            start_time = time.time()
            while time.time() - start_time < 15:  # Run for 15 seconds
                electro.read_hall_sensor()  # Run Hall sensor
                time.sleep(1)  # Wait for 1 second between readings (to avoid overwhelming the terminal)

        elif key == ord('g'):
            stdscr.clear()
            stdscr.addstr(0, 0, "Running Gas sensor test for 15 seconds...")
            stdscr.refresh()

            start_time = time.time()
            while time.time() - start_time < 15:  # Run for 15 seconds
                gas.read_gas_sensor()  # Run Gas sensor
                time.sleep(1)  # Wait for 1 second between readings (to avoid overwhelming the terminal)

        elif key == ord('a'):  # For the Gyroscope/Accelerometer
            stdscr.clear()
            stdscr.addstr(0, 0, "Running Gyroscope/Accelerometer test for 15 seconds...")
            stdscr.refresh()

            start_time = time.time()
            while time.time() - start_time < 15:  # Run for 15 seconds
                gyroaccel.read_gyroaccel()  # Run Gyroscope/Accelerometer
                time.sleep(1)  # Wait for 1 second between readings (to avoid overwhelming the terminal)

        elif key == ord('q'):
            break  # Exit the loop if 'q' is pressed

        time.sleep(0.1)  # Prevent high CPU usage

    GPIO.cleanup()  # Clean up GPIO when exiting

# Start the Curses UI
curses.wrapper(main)
