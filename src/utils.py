import src.modules.console as console
import src.modules.keyboard as keyboard

name = ''

def quitGame():
    console.reset(1, 1, 30, 150)
    quit()

def getSavedName():
    return name