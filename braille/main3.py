from doubleDisplay import doubleDisplay




def main():

    HK = doubleDisplay()

    while(True):
        sig = HK.readChars()
        
        #if at EOF break out
        if sig == 0:
            break



main()
