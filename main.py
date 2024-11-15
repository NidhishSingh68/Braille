import time

class characterParser:
    def __init__(self , textFile):
        self.fileHandler = open(textFile,"r")
        self.lineContainer = self.fileHandler.readline()
        self.characterTracker = -1

    def getNextCharacter(self):


        self.characterTracker +=1
        if (self.lineContainer[self.characterTracker] == "\n"):
            self.lineContainer = self.fileHandler.readline()
            self.characterTracker = -1 #reinitalize it to the beginning

        #Return the empty character if at EOF 
        if(self.lineContainer == ""):
            return self.lineContainer



        return self.lineContainer[self.characterTracker] # return character at the index characterTracker
    
    def setDelay(self, delay ):

        self.delay = delay # set the delay time, Could potentially be changed in RT
    
    #This function will read every character of the file until the EOF
    def readWithDelay(self):
        
        while(True):

            c = self.getNextCharacter()
            if( c==""):
                break
            else:
                print(c)

            time.sleep(self.delay)


        
    
def main():
    characterIterator = characterParser("test.txt")
    characterIterator.setDelay(0)
    characterIterator.readWithDelay()



main()






