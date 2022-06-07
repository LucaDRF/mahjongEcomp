from math import floor
from time import sleep, time
import src.pecas as pecas
from src.ranking import calcPoints
import src.modules.console as console
import src.modules.keyboard as keyboard
import src.style as style
import src.timer as timer
import src.utils as utils

def printGameEasy():
    pecasRetiradas = 0

    console.init(30)
    console.reset(1,1,30,150)
    style.printGamestyle(40)
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
                console.reset(1,1,30,150)
                calcPoints(round(currentTime - firstTime), 'easy', pecasRetiradas, 38, True)
                sleep(5)
                break

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
                    print('\033[1;34;40m' + chr(9600) + '\033[1;37;40m')

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
                sleep(5)
                break

            if (pecasRetiradas == 38):
                console.reset(1,1,30,150)
                calcPoints(round(currentTime - firstTime), 'easy', pecasRetiradas, 38)
                if(event.name == 'enter'):
                    break
                break

def printGameMedium():
    pecasRetiradas = 0

    console.init(30)
    console.reset(1,1,30,150)
    style.printGamestyle(50)
    positionsAll = pecas.randomizeMediumPecas()
    positionsLayer1 = positionsAll[0]
    positionsLayer2 = positionsAll[1]
    positionY = 0
    positionX = 0
    x = 62
    y = 10
    console.gotoxy(x, y)

    selectedX = 0
    selectedY = 0
    selectedSimbol = 0
    selectedSimbolIsLevelOne = 0

    firstTime = time()

    while True:
        currentTime = time()
        event = keyboard.read_event()

        totalY = len(positionsLayer1) - 1

        isLevelOne = bool(not positionsLayer2[positionY][positionX]) and bool(positionsLayer1[positionY][positionX])
        upLines = positionY == 0 or positionY == totalY
        midLines = 0 < positionY < totalY
        pecaValida = 0

        if (isLevelOne):
            samePecas = selectedSimbol == positionsLayer1[positionY][positionX]
            pecaValida = not positionsLayer1[positionY][positionX + 1] or not positionsLayer1[positionY][positionX - 1]
        else:
            samePecas = selectedSimbol == positionsLayer2[positionY][positionX]
            pecaValida = not positionsLayer2[positionY][positionX + 1] or not positionsLayer2[positionY][positionX - 1]

        pecaSelected = selectedX == x and selectedY == y

        if(event.event_type == keyboard.KEY_DOWN):
            if (event.name == 'right' and ((upLines and positionX < 8) or (midLines and positionX < 9))):
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
                console.reset(1,1,30,150)
                calcPoints(round(currentTime - firstTime), 'easy', pecasRetiradas, 38, True)
                sleep(5)
                break

            elif (event.name == 'enter' and positionsLayer1[positionY][positionX] and pecaValida and not pecaSelected):
                if (not samePecas and selectedSimbol):
                    console.gotoxy(x, y - 1)
                    print(' ')
                    console.gotoxy(selectedX, selectedY - 1)
                    print(' ')
                    selectedX = 0
                    selectedY = 0
                    selectedSimbol = 0
                    selectedSimbolIsLevelOne = 0
                elif (samePecas):
                    console.reset(1,6,50,150)
                    positionsAll = pecas.removePecaTrid(positionsAll, floor((selectedX - 62) / 5), floor((selectedY - 10) / 4), selectedSimbolIsLevelOne, positionX, positionY, isLevelOne)
                    positionsLayer1 = positionsAll[0]
                    positionsLayer2 = positionsAll[1]
                    pecasRetiradas += 2
                    selectedX = 0
                    selectedY = 0
                    selectedSimbol = 0
                else:
                    console.gotoxy(x, y - 1)
                    selectedX = x
                    selectedY = y
                    selectedSimbolIsLevelOne = isLevelOne

                    if (isLevelOne):
                        selectedSimbol = positionsLayer1[positionY][positionX]
                    else:
                        selectedSimbol = positionsLayer2[positionY][positionX]

                    print('\033[1;34;40m' + chr(9600) + '\033[1;37;40m')

            elif (event.name == 'enter' and pecaSelected):
                console.gotoxy(x, y - 1)
                selectedX = 0
                selectedY = 0
                selectedSimbol = 0
                selectedSimbolIsLevelOne = 0
                print(' ')


            timer.countdown(currentTime - firstTime)

            console.gotoxy(x, y)

            if (currentTime - firstTime) / 60 >= 15:
                console.reset(1,1,30,150)
                print('TEMPO ACABOU!')
                sleep(5)
                break

            if (pecasRetiradas == 38):
                console.reset(1,1,30,150)
                calcPoints(round(currentTime - firstTime), 'easy', pecasRetiradas, 38)
                sleep(5)
                break



