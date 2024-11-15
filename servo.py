from adafruit_servokit import ServoKit
from time import sleep

# Initialize the ServoKit for 16-channel PWM driver
kit = ServoKit(channels=16)

# Example: Control servos on channels 0 and 1
try:
    while True:
        print("Moving servos to 0°")
        kit.servo[0].angle = 0  # Set servo on channel 0 to 0°
        kit.servo[1].angle = 0  # Set servo on channel 1 to 0°
        sleep(1)

        print("Moving servos to 90°")
        kit.servo[0].angle = 90  # Set servo on channel 0 to 90°
        kit.servo[1].angle = 90  # Set servo on channel 1 to 90°
        sleep(1)

        print("Moving servos to 180°")
        kit.servo[0].angle = 180  # Set servo on channel 0 to 180°
        kit.servo[1].angle = 180  # Set servo on channel 1 to 180°
        sleep(1)

except KeyboardInterrupt:
    print("Exiting program")
