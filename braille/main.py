from parseFile import characterParser

from display import display


def main():
    #create a display object
    file =  characterParser("./test.txt")
    disp = display(10,1)
    while(True):
        char = file.readWithDelay()
        #if an empty string returned(When at EOF) exit the application
        if char == "":
            break
        else:
            disp.display(char)
    



main()
