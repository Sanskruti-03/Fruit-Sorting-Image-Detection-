import RPi.GPIO as GPIO
import time

# Function to move the motor continuously for a given duration
def move_motor(duration, direction='forward', speed=50):
    # Set GPIO pins
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # Motor pins
    MotorA = 27  # Pin for Motor A
    MotorB = 17  # Pin for Motor B

    # Setup GPIO pins
    GPIO.setup(MotorA, GPIO.OUT)
    GPIO.setup(MotorB, GPIO.OUT)

    # Create PWM object for motor speed control
    motor_pwm = GPIO.PWM(MotorA, 100)
    motor_pwm.start(0)
    
    # Set the motor direction
    if direction == 'forward':
        GPIO.output(MotorA, GPIO.HIGH)
        GPIO.output(MotorB, GPIO.LOW)
    else:
        GPIO.output(MotorA, GPIO.LOW)
        GPIO.output(MotorB, GPIO.HIGH)
    
    # Set the motor speed
    duty_cycle = min(max(0, speed), 100)
    motor_pwm.ChangeDutyCycle(duty_cycle)
    
    # Run the motor for the given duration
    start_time = time.time()
    while (time.time() - start_time) < duration:
        time.sleep(1)
    
    # Stop the motor
    motor_pwm.stop()
    GPIO.output(MotorA, GPIO.LOW)
    GPIO.output(MotorB, GPIO.LOW)

    # Cleanup GPIO pins
    GPIO.cleanup()

# Move the motor forward continuously at 50% speed for 10 seconds
move_motor(duration=10, direction='forward', speed=50)


