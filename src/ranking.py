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

    style.printRankingStyle(50)

    console.gotoxy(65, 35)

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
    pecasPoints = round(2000 * (pecasRet / totalPecas))
    timePoints = 0

    if (quit):
        timePoints = 100
    elif (timeSpent <= 300):
        timePoints = 3000 - timeSpent
    elif (300 < timeSpent < 600):
        timePoints = 2000 - timeSpent
    elif (timeSpent < 900):
        timePoints = 1000 - timeSpent

    totalPoints = round(difficultyPoints[difficulty] + pecasPoints + timePoints)
    addPlayer(name, totalPoints)
    printPoints(name, timeSpent, timePoints, difficulty, pecasRet, totalPecas)

def printPoints(name, timeSpent, timePoints, difficulty, pecasRet, totalPecas):
    console.init(30)
    console.reset(1, 1, 30, 150)
    timeRemaining = 900 - timeSpent
    style.printPointsStyle()
    style.printText('N/O/M/E/:', name, 50, 10)
    difficultyWriting = { 'hard': ['DIFÍCIL', 2000, ''], 'medium': ['MÉDIO', 1000, ''], 'easy': ['FÁCIL', 500, '38'] }
    sleep(0.7)
    style.printText('D/I/F/I/C/U/L/D/A/D/E/:', difficultyWriting[difficulty][0], 50, 12)
    sleep(0.7)
    style.printText('T/E/M/P/O/ /R/E/S/T/A/N/T/E/:','{min}:{seg}'.format(min = floor(timeRemaining / 60), seg = timeRemaining % 60), 50, 14)
    sleep(0.7)
    style.printText('P/E/Ç/A/S/ /R/E/T/I/R/A/D/A/S/:','{pecas}/{totalPecas}'.format(pecas = pecasRet, totalPecas = totalPecas), 50, 16)
    sleep(0.7)
    style.printText('P/O/N/T/U/A/Ç/Ã/O/ /D/E/ /D/I/F/I/C/U/L/D/A/D/E/:', str(difficultyWriting[difficulty][1]), 50, 18)
    sleep(0.7)
    style.printText('P/O/N/T/U/A/Ç/Ã/O/ /D/E/ /T/E/M/P/O/:',str(timePoints),50, 20)
    sleep(0.7)
    style.printText('P/O/N/T/U/A/Ç/Ã/O/ /D/E/ /P/E/Ç/A/S/:', str(round(2000 * pecasRet / totalPecas)), 50, 22)
    sleep(0.7)
    style.printText('P/O/N/T/U/A/Ç/Ã/O/ /T/O/T/A/L/:', difficultyWriting[difficulty][1] + timePoints + round(2000 * pecasRet / totalPecas), 50, 26)
    

