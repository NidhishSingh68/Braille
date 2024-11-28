from adafruit_servokit import ServoKit
import time
from pin import pin
class display:
    def __init__(self , delay : int , index : int):
        self.kit = ServoKit(channels=16)
        self.braille_table = {
            ' ': '000000',
            'a': '100000',
            'b': '110000',
            'c': '100100',
            'd': '100110',
            'e': '100010',
            'f': '110100',
            'g': '110110',
            'h': '110010',
            'i': '010100',
            'j': '010110',
            'k': '101000',
            'l': '111000',
            'm': '101100',
            'n': '101110',
            'o': '101010',
            'p': '111100',
            'q': '111110',
            'r': '111010',
            's': '011100',
            't': '011110',
            'u': '101001',
            'v': '111001',
            'w': '010111',
            'x': '101101',
            'y': '101111',
            'z': '101011',
            '#': '001111', # this appears before a number is shown
            '1': '100000',
            '2': '110000',
            '3': '100100',
            '4': '100110',
            '5': '100010',
            '6': '110100',
            '7': '110110',
            '8': '110010',
            '9': '010100',
            '0': '010110',
            ' ': '000000',
            '!': '110100',
            ',': '100000',
            '.': '010011',
            '?': '011001',
            '&': '010000',
            ':': '010010',
            ';': '011000',
            '-': '001001',
            '(': '110001',
            ')': '001110',
            '*': '111111'
        }
        
        self.delay = delay 
        self.rotationAngle = 10
        self.eqmAngle      = 90
        self.pinGap          = 0
        self.pinArray = []
        if index == 0:
            for i in range(0,6):
                if i == 0:
                    self.pinArray.append(pin(110,77))
                if i == 1:
                    self.pinArray.append(pin(60,87))
                if i == 2:
                    self.pinArray.append(pin(83,107))
                if i == 3 or i == 4:
                    self.pinArray.append(pin(110,86))
                if i == 5:
                    self.pinArray.append(pin(83,107))
        if index == 1:
            self.pinGap =   6
            for i in range(0,6):
                if i == 1 :
                    pinO = pin(110,85) 
                    self.pinArray.append(pinO)
                if i == 2:
                    pinO = pin(110,79)
                    self.pinArray.append(pinO)

                if i == 3:
                    pinO = pin(100,123)
                    self.pinArray.append(pinO)
                if i == 0:
                    pinO = pin(80,112)
                    self.pinArray.append(pinO)

                if  i == 4:
                    pinO = pin(75,108)
                    self.pinArray.append(pinO)
                if i == 5:
                    pinO = pin(90,53)
                    self.pinArray.append(pinO)
                    
            
    #reset the positions of all the servos to origin
    def reset(self):
        for i in range(0,6):
            self.kit.servo[i + self.pinGap].angle = self.pinArray[i].getEqmAngle()    
        time.sleep(0.1)
    def display(self, character):
        #Call the reset function before displaying anything everytime
        #self.reset()
        if character in self.braille_table:
            pattern = self.braille_table[character]
            for i in range(0,6):
                #print(pattern[i])
                # If its a 1 move the corresponding servo
                if pattern[i] == '1':
                    #move the first 3 servos clockwise

                    self.kit.servo[i + self.pinGap].angle = self.pinArray[i].getUpPosition()
                else:
                    #if character is 0, revert back to the eqm position
                    self.kit.servo[i+self.pinGap].angle = self.pinArray[i].getEqmAngle()
            #delay for sometime after displaying
            if self.pinGap !=0:
                time.sleep(self.delay)
                


            




