from time import sleep
from math import floor
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

def addPlayer(name = 'unknown', points = 0):
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
    console.reset(1, 1, 30, 150)

    sleep(0.5)

    showRanking()

    console.gotoxy(68, 35)
    print(chr(9487) + chr(9473)*15 + chr(9491))
    console.gotoxy(68, 36)
    print(chr(9475) + ' '*15 + chr(9475))
    console.gotoxy(68, 37)
    print(chr(9475) + '     Voltar    ' + chr(9475))
    console.gotoxy(68, 38)
    print(chr(9475) + ' '*15 + chr(9475))
    console.gotoxy(68, 39)
    print(chr(9495) + chr(9473)*15 + chr(9499))

    style.printRankingStyle(50)

    console.gotoxy(76, 37)

def printRanking():
    menu()

    while True:
        keyPressed = keyboard.read_key()

        if (keyPressed == 'enter'):
            console.reset(1, 1, 30, 150)
            break

def calcPoints(timeSpent, difficulty, pecasRet, totalPecas, quit = False):
    name = utils.getSavedName()
    difficultyPoints = { 'hard': 2000, 'medium': 1000, 'easy': 500 }
    pecasPoints = { 'hard': 25, 'medium': 20, 'easy': 15}
    timePoints = 0

    if (timeSpent <= 100 and quit):
        timePoints = 100
    elif (timeSpent <= 300):
        timePoints = 3000 - timeSpent
    elif (300 < timeSpent < 600):
        timePoints = 2000 - timeSpent
    elif (600 <= timeSpent < 900):
        timePoints = 1000 - timeSpent

    totalPoints = round(difficultyPoints[difficulty] + pecasPoints[difficulty]*pecasRet + timePoints)
    addPlayer(name, totalPoints)
    printPoints(name, timeSpent, timePoints, difficulty, pecasRet, totalPecas, pecasPoints)

def printPoints(name, timeSpent, timePoints, difficulty, pecasRet, totalPecas, pecasPoints):
    console.init(30)
    console.reset(1, 1, 30, 150)
    timeRemaining = 900 - timeSpent
    style.printPointsStyle()
    style.printText('N/O/M/E/:', name, 65, 10)
    difficultyWriting = { 'hard': ['DIFÍCIL', 2000, ''], 'medium': ['MÉDIO', 1000, ''], 'easy': ['FÁCIL', 500, '38'] }
    sleep(0.4)
    style.printText('D/I/F/I/C/U/L/D/A/D/E/:', difficultyWriting[difficulty][0], 65, 12)
    sleep(0.4)
    style.printText('T/E/M/P/O/ /R/E/S/T/A/N/T/E/:','{min}:{seg}'.format(min = floor(timeRemaining / 60), seg = ('0' + str(timeRemaining % 60) if timeRemaining % 60 < 10 else str(timeRemaining % 60))), 65, 14)
    sleep(0.4)
    style.printText('P/E/Ç/A/S/ /R/E/T/I/R/A/D/A/S/:','{pecas}/{totalPecas}'.format(pecas = pecasRet, totalPecas = totalPecas), 65, 16)
    sleep(0.4)
    style.printText('P/O/N/T/U/A/Ç/Ã/O/ /D/E/ /D/I/F/I/C/U/L/D/A/D/E/:', str(difficultyWriting[difficulty][1]), 65, 18)
    sleep(0.4)
    style.printText('P/O/N/T/U/A/Ç/Ã/O/ /D/E/ /T/E/M/P/O/:',str(timePoints),65, 20)
    sleep(0.4)
    style.printText('P/O/N/T/U/A/Ç/Ã/O/ /D/E/ /P/E/Ç/A/S/:', pecasPoints[difficulty]*pecasRet, 65, 22)
    sleep(0.4)
    style.printText('P/O/N/T/U/A/Ç/Ã/O/ /T/O/T/A/L/:', difficultyWriting[difficulty][1] + timePoints + pecasPoints[difficulty]*pecasRet, 65, 26)
    sleep(0.4)
    style.printText('P/r/e/s/s/i/o/n/e/ /E/n/t/e/r/ /p/a/r/a/ /A/v/a/n/ç/a/r/././.', ' ', 110, 26)
    console.gotoxy(141,26)