# CMPT 120 Yet Another Image Processer
# Starter code for main.py
# Author(s): Tanjodh Hayer, Inderpreet Rangi
# Date: December 7th, 2020
# Description: An image processor which takes in a user input to manipulate a certain image

import cmpt120imageProj
import cmpt120imageManip
import tkinter.filedialog
import pygame
pygame.display.init()
pygame.font.init()

# list of system options
system = [
            "Q: Quit",
         ]

# list of basic operation options
basic = [
          " I: Switch to Intermeidate Functions",
          " A: Switch to Advanced Functions"
         ]

# list of intermediate operation options
intermediate = [
                  " B: Switch to Basic Functions",
                  " A: Switch to Advanced Functions"
                 ]

# list of advanced operation options
advanced = [
                " B: Switch to Basic Functions",
                " I: Switch to Intermediate Functions"
             ]

# a helper function that generates a list of strings to be displayed in the interface
def generateMenu(state):
    """
    Input:  state - a dictionary containing the state values of the application
    Returns: a list of strings, each element represets a line in the interface
    """
    menuString = ["Welcome to CMPT 120 Image Processer!"]
    menuString.append("") # an empty line
    menuString.append("Choose the following options:")
    menuString.append("")
    menuString += system
    menuString.append("O: Open Image")
    menuString.append("S: Save Current Image")
    menuString.append("R: Reload Original Image")
    menuString.append("") # an empty line

    # build the list differently depending on the mode attribute
    if state["mode"] == "basic":
        menuString.append("--Basic Mode--")
        menuString.append("1: Invert")
        menuString.append("2: Flip Horizontal")
        menuString.append("3: Flip Verticle")
        menuString += basic
        menuString.append("Enter your choice, (Q/O/S/R or 1-3 or I/A)")
    elif state["mode"] == "intermediate":
        menuString.append("--Intermediate Mode--")
        menuString.append("1: Remove Red Channel")
        menuString.append("2: Remove Green Channel")
        menuString.append("3: Remove Blue Channel")
        menuString.append("4: Convert to GrayScale")
        menuString.append("5: Apply Sepia Filter")
        menuString.append("6: Decrease Brightness")
        menuString.append("7: Increase Brightness")
        menuString += intermediate
        menuString.append("Enter your choice, (Q/O/S/R or 1-7 or B/A)")
    elif state["mode"] == "advanced":
        menuString.append("--Advanced Mode--")
        menuString.append("1: Rotate left")
        menuString.append("2: Rotate Right")
        menuString.append("3: Pixelate")
        menuString.append("4: Binarize")
        menuString += advanced
        menuString.append("Enter your choice, (Q/O/S/R or 1-4 or B/I)")
    else:
        menuString.append("Error: Unknown mode!")

    return menuString
# a helper function that returns the result image as a result of the operation chosen by the user
# it also updates the state values when necessary (e.g, the mode attribute if the user switches mode)
def handleUserInput(state, img):
    """
        Input:  state - a dictionary containing the state values of the application
                img - the 2d array of RGB values to be operated on
        Returns: the 2d array of RGB vales of the result image of an operation chosen by the user
    """
    userInput = state["lastUserInput"].upper()
    # handle the system functionalities
    if userInput.isalpha(): # check if the input is an alphabet
        print("Log: Doing system functionalities " + userInput)
        
        if userInput == "Q": # this case actually won't happen, it's here as an example
            print("Log: Quitting...")
        
        
        elif userInput == "O":
          tkinter.Tk().withdraw()
          openedFile = tkinter.filedialog.askopenfilename()

          appStateValues["lastOpenFilename"] = openedFile

          img = cmpt120imageProj.getImage(openedFile) 

          cmpt120imageProj.showInterface(img, "Opened Image", generateMenu(appStateValues))
            
        # if user types S, save the file
        elif userInput == "S":
          tkinter.Tk().withdraw()
          savedFile = tkinter.filedialog.asksaveasfilename()

          appStateValues["lastSaveFilename"] = cmpt120imageProj.saveImage(img , savedFile)
          
        # if user types R, reload the original file
        elif userInput == "R":
          img = cmpt120imageProj.getImage(appStateValues["lastOpenFilename"])   

          cmpt120imageProj.showInterface(img, "Reload Image", generateMenu(appStateValues))
        
        elif userInput == "I":
            state["mode"] = "intermediate"
            cmpt120imageProj.showInterface(img, "Intermediate", generateMenu(appStateValues))
        
        elif userInput == "A":
            state['mode'] = "advanced"
            cmpt120imageProj.showInterface(img, "advanced", generateMenu(appStateValues))
        
        elif userInput == "B":
            state["mode"] = "basic"
            cmpt120imageProj.showInterface(img, "basic", generateMenu(appStateValues))
          
        else: # unrecognized user input
            print("Log: Unrecognized user input: " + userInput)
        # ***add the rest to handle other system functionalities***

    # or handle the manipulation functionalities based on which mode the application is in
    elif userInput.isdigit(): # has to be a digit for manipulation options
        print("Log: Doing manipulation functionalities " + userInput)
        
        if state['mode'] == "basic":
         
          if userInput == "1":
            img = cmpt120imageManip.invert(img)
            cmpt120imageProj.showInterface(img, "Invert", generateMenu(appStateValues))
         
          elif userInput == "2":
            img = cmpt120imageManip.flipHorizontal(img)
            cmpt120imageProj.showInterface(img, "flipHorizontal", generateMenu(appStateValues))
         
          elif userInput == "3":
            img = cmpt120imageManip.flipVertical(img)
            cmpt120imageProj.showInterface(img, "flipVerticle", generateMenu(appStateValues))

          else: # unrecognized user input
            print("Log: Unrecognized user input: " + userInput) 

        if state['mode'] == "intermediate":
          
          if userInput == "1":
            img = cmpt120imageManip.red(img)
            cmpt120imageProj.showInterface(img, "red", generateMenu(appStateValues))
          
          elif userInput == "2":
            img = cmpt120imageManip.green(img)
            cmpt120imageProj.showInterface(img, "green", generateMenu(appStateValues))
          
          elif userInput == "3":
            img = cmpt120imageManip.blue(img)
            cmpt120imageProj.showInterface(img, "blue", generateMenu(appStateValues))
          
          elif userInput == "4":
            img = cmpt120imageManip.greyscale(img)
            cmpt120imageProj.showInterface(img, "greyscale", generateMenu(appStateValues))

          elif userInput == "5":
           img = cmpt120imageManip.sepia(img)
           cmpt120imageProj.showInterface(img, "sepia", generateMenu(appStateValues))
          
          elif userInput == "6":
            img = cmpt120imageManip.decrease_brightness(img)
            cmpt120imageProj.showInterface(img, "decrease_brightness", generateMenu(appStateValues))
          
          elif userInput == "7":
            img = cmpt120imageManip.increase_brightness(img)
            cmpt120imageProj.showInterface(img, "increase_brightness", generateMenu(appStateValues))
          
          else: # unrecognized user input
            print("Log: Unrecognized user input: " + userInput)

        if state['mode'] == "advanced":
          
          if userInput == "1":
            img = cmpt120imageManip.RotateLeft(img)
            cmpt120imageProj.showInterface(img, "rotateleft", generateMenu(appStateValues))
          
          elif userInput == "2":
            img = cmpt120imageManip.RotateRight(img)
            cmpt120imageProj.showInterface(img, "rotateright", generateMenu(appStateValues)) 
          
          elif userInput == "3":
            img = cmpt120imageManip.pixelate(img)
            cmpt120imageProj.showInterface(img, "pixelate", generateMenu(appStateValues)) 
          
          elif userInput == "4":
            img = cmpt120imageManip.binarize(img)
            cmpt120imageProj.showInterface(img, "binarize", generateMenu(appStateValues)) 
          
          else: # unrecognized user input
            print("Log: Unrecognized user input: " + userInput)
      
    else: # unrecognized user input
            print("Log: Unrecognized user input: " + userInput)
    return img

# use a dictionary to remember several state values of the application
appStateValues = {
                    "mode": "basic",
                    "lastOpenFilename": "",
                    "lastSaveFilename": "",
                    "lastUserInput": ""
                 }


currentImg = cmpt120imageProj.createBlackImage(600, 400) # create a default 600 x 400 black image
cmpt120imageProj.showInterface(currentImg, "No Image", generateMenu(appStateValues)) # note how it is used


# ***this is the event-loop of the application. Keep the remainder of the code unmodified***
keepRunning = True
# a while-loop getting events from pygame
while keepRunning:
    ### use the pygame event handling system ###
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            appStateValues["lastUserInput"] = pygame.key.name(event.key)
            # prepare to quit the loop if user inputs "q" or "Q"
            if appStateValues["lastUserInput"].upper() == "Q":
                keepRunning = False
            # otherwise let the helper function handle the input
            else:
                currentImg = handleUserInput(appStateValues, currentImg)
        elif event.type == pygame.QUIT: #another way to quit the program is to click the close botton
            keepRunning = False

# shutdown everything from the pygame package
pygame.quit()

print("Log: Program Quit")