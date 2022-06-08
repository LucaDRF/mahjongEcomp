import src.modules.console as console
import src.modules.keyboard as keyboard

name = ''

def quitGame():
    console.reset(1, 1, 30, 150)
    quit()

def getSavedName():
    return name

def skipAction():
    while True:
        event2 = keyboard.read_event()
        if(event2.event_type == keyboard.KEY_DOWN):
            if(event2.name == 'enter'):
                break


