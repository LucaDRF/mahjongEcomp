from math import floor
from time import sleep, time
import src.pecas as pecas
import src.modules.console as console
import src.modules.keyboard as keyboard
import src.style as style
import src.timer as timer

def quitGame():
    console.reset(1, 1, 30, 150)
    quit()

def printGame():
    pecasRetiradas = 0

    console.init(30)
    console.reset(1,1,30,150)
    style.printGamestyle()
    positions = pecas.randomizePecas()
    positionY = 0
    positionX = 0
    x = 62
    y = 10
    console.gotoxy(x, y)

    selectedX = 0
    selectedY = 0
    selectedSimbol = 0

    firstTime = time()

    while True:
        currentTime = time()
        event = keyboard.read_event()

        totalY = len(positions) - 1

        upLines = positionY == 0 or positionY == totalY
        midLines = 0 < positionY < totalY
        pecaValida = not positions[positionY][positionX + 1] or not positions[positionY][positionX - 1]
        pecaSelected = selectedX == x and selectedY == y
        samePecas = selectedSimbol == positions[positionY][positionX]

        if(event.event_type == keyboard.KEY_DOWN):
            if (event.name == 'right' and ((upLines and positionX < 6) or (midLines and positionX < 7))):
                positionX += 1
                x += 5

            elif (event.name == 'left' and ((upLines and positionX > 2) or (midLines and positionX > 1))):
                positionX -= 1
                x -= 5

            elif (event.name == 'up' and positionY > 0):
                positionY -= 1
                y -= 4
        
            elif (event.name == 'down' and positionY < totalY):
                positionY += 1
                y += 4

            elif (event.name == 'esc'):
                quitGame()

            elif (event.name == 'enter' and positions[positionY][positionX] and pecaValida and not pecaSelected): 
                if (not samePecas and selectedSimbol):
                    console.gotoxy(x, y - 1)
                    print(' ')
                    console.gotoxy(selectedX, selectedY - 1)
                    print(' ')
                    selectedX = 0
                    selectedY = 0
                    selectedSimbol = 0
                elif (samePecas):
                    console.reset(1,6,30,150)
                    positions = pecas.removePeca(positions, floor((selectedX - 62) / 5), floor((selectedY - 10) / 4), positionX, positionY)
                    pecasRetiradas += 2
                    selectedX = 0
                    selectedY = 0
                    selectedSimbol = 0
                else:
                    console.gotoxy(x, y - 1)
                    selectedX = x
                    selectedY = y
                    selectedSimbol = positions[positionY][positionX]
                    print(chr(71110))

            elif (event.name == 'enter' and pecaSelected):
                console.gotoxy(x, y - 1)
                selectedX = 0
                selectedY = 0
                selectedSimbol = 0
                print(' ')


            timer.countdown(currentTime - firstTime)

            console.gotoxy(x, y)

            if (currentTime - firstTime) / 60 >= 15:
                console.reset(1,1,30,150)
                print('TEMPO ACABOU!')
                sleep(10)
                break

