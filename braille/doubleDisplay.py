
from display import display

from parseFile import characterParser


class doubleDisplay:
    def __init__(self):

        self.fileHandler = characterParser("./test2.txt")
        #initialize both the displays
        self.disp1      = display(10,0) 
        self.disp2      = display(10,1)
    def readChars(self):
        char1 = self.fileHandler.readWithDelay()

        char2 = self.fileHandler.readWithDelay()

        if char1 == "" or char2 == "":
            return 0
        # both are characters, proceed as normal
        if not char1.isnumeric() and not char2.isnumeric():
            self.disp1.display(char1)
            self.disp2.display(char2)

        if char1.isnumeric():
            self.disp1.display('#')
            self.disp2.display(char2)
            self.fileHandler.goBack()

        if char2.isnumeric():
            self.disp1.display(char1)
            self.disp1.display(' ')
            self.fileHandler.goBack()

        return 1



