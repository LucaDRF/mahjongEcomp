from time import sleep
import src.modules.console as console
import src.modules.keyboard as keyboard
import src.style as style
import src.utils as utils

def startRanking():
    arq = open('ranking.txt', 'w')

    arq.write('\n\n\n\n')

    arq.close

def readRanking():
    try:
        arq = open('ranking.txt', 'r')
    except:
        startRanking()
        arq = open('ranking.txt', 'r')
    finally:
        return arq.read()

def addPlayer(name: 'unknown', points):
    arq = readRanking()
    lines = arq.split('\n')

    for index in range(0, len(lines)):
        items = lines[index].split(' | ')

        if len(items) != 2:
            lines[index] = name + ' | ' + str(points) + ' pontos'
            break

        playerPoints = int(items[1].split(' ')[0])

        if (points > playerPoints):
            lines.insert(index, name + ' | ' + str(points) + ' pontos')
            break

    if len(lines) > 5:
        lines.pop()

    arq = open('ranking.txt', 'w')
    arq.writelines('\n'.join(lines))

def showRanking():
    arq = readRanking()
    lines = arq.split('\n')
    ranking = ''

    for cont in range(0, 5):
        console.gotoxy(52, 13 + (cont * 3))
        print('_'*50)
        console.gotoxy(65, 15 + (cont * 3))
        print(('| {order}. {ranking} |'.format(order = cont + 1, ranking = lines[cont])))
        console.gotoxy(52, 16 + (cont * 3))
        print('_'*50)

    print(ranking)

def menu():
    console.init(30)
    console.reset(1, 1, 30, 120)

    sleep(0.5)

    showRanking()

    console.gotoxy(65, 35)
    print(chr(9487) + chr(9477)*15 + chr(9491))
    console.gotoxy(65, 36)
    print(chr(9479) + ' '*15 + chr(9479))
    console.gotoxy(65, 37)
    print(chr(9479) + '     Voltar    ' + chr(9479))
    console.gotoxy(65, 38)
    print(chr(9479) + ' '*15 + chr(9479))
    console.gotoxy(65, 39)
    print(chr(9495) + chr(9477)*15 + chr(9498))

    style.printStyle(50)
    console.gotoxy(73, 6)
    print('\033[1;35;40mRANKING')

    console.gotoxy(65, 35)

def printRanking():
    menu()

    while True:
        keyPressed = keyboard.read_key()

        if (keyPressed == 'enter'):
            console.reset(1, 1, 30, 150)
            break

def calcPoints(timeRemaining, difficulty, percPecas):
    name = utils.getSavedName()
    difficultyPoints = { 'hard': 2000, 'medium': 1000, 'easy': 500 }
    pecasPoints = 2000 * percPecas
    timePoints = 0

    if (timeRemaining <= 300):
        timePoints = 4000 - timeRemaining
    elif (300 < timeRemaining < 600):
        timePoints = 3000 - timeRemaining
    elif (timeRemaining < 900):
        timePoints = 2000 - timeRemaining

    totalPoints = round(difficultyPoints[difficulty] + pecasPoints + timePoints)
    addPlayer(name, totalPoints)
    return name
