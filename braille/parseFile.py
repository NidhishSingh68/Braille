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

        #Return empty character if at EOF 
        if(self.lineContainer == ""):
            return self.lineContainer
        return self.lineContainer[self.characterTracker] # return character at the index characterTracker
    def goBack(self):
        self.characterTracker = self.characterTracker - 1
    #This function will read every character of the file until the EOF
    def readWithDelay(self):
        c = self.getNextCharacter()
        print(c)
        return c
    









