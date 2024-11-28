import time
from display import display
from adafruit_servokit import ServoKit
#initalize with 1 second delay
display = display(0.5, 1)
#display.display('*')
#time.sleep(0.5)
display.reset()
display.display('l')
time.sleep(1)
display.reset()

#display.display('a')
#display.display('w')



#kit = ServoKit(channels=16)

#kit.servo[0].angle = 85

#time.sleep(0.5)

#kit.servo[0].angle = 100



#kit.servo[0].angle = 90

#kit.servo[0].angle = 70
