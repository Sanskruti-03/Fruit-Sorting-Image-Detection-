import RPi.GPIO as GPIO
import time

def move_servo(position):
    # Set up the GPIO pins
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)

    # Create a PWM instance
    pwm = GPIO.PWM(17, 50)  # PWM frequency of 50 Hz

    # Calculate the duty cycle based on the desired position
    duty_cycle = 2.5 + (position / 18)

    # Move the servo to the desired position
    pwm.start(duty_cycle)
    time.sleep(1)

    # Clean up the GPIO pins
    pwm.stop()
    GPIO.cleanup()

# Move the servo to the 0 degree position
move_servo(0)

# Move the servo to the 90 degree position
#move_servo(90)

# Move the servo to the 180 degree position
#move_servo(180)
