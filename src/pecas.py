from random import choice
import src.modules.console as console

def printPeca(x, y, peca):

    console.gotoxy(x, y)

    print(chr(9487) + chr(9477)*3 + chr(9491))

    console.gotoxy(x, y+1)
    print(chr(9479) + '   ' + chr(9479))

    console.gotoxy(x, y+2)

    print(chr(9479) + ' '*3 + chr(9479)) 

    console.gotoxy(x, y+3)

    print(chr(9479) + '   ' + chr(9479))

    console.gotoxy(x, y+4)

    print(chr(9495) + chr(9477)*3 + chr(9498))  

    console.gotoxy(x+2, y+2)
    print(peca)

def randomizePecas():
    simbols = [10057, 10057, 10057, 10057, 10010, 10010, 10010, 10010, 9819, 9819, 9819, 9819, 9851, 9851, 9851, 9851, 12745, 12745, 12745, 12745, 43111, 43111, 43111, 43111, 43124, 43124, 43124, 43124, 675, 675, 675, 675, 643, 643, 643, 643]

    x = 60
    y = 8

    for contX in range(9):
        for contY in range(4):
            simbol = choice(simbols)
            printPeca(x + (contX * 5), y + (contY * 4), chr(simbol))
            simbols.remove(simbol)
