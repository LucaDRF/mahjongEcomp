import src.modules.console as console
from time import sleep

def printBarras(heitgh):
    console.gotoxy(1,1)
    print('\033[1;37;40m_'*150)

    console.gotoxy(1,heitgh)
    print('\033[1;37;40m_'*150)

def printMenuTitle():
    console.gotoxy(50,5)
    print('███╗   ███╗ █████╗ ██╗  ██╗     ██╗ ██████╗ ███╗   ██╗ ██████╗')
    console.gotoxy(50,6)
    print('████╗ ████║██╔══██╗██║  ██║     ██║██╔═══██╗████╗  ██║██╔════╝')
    console.gotoxy(50,7)
    print('██╔████╔██║███████║███████║     ██║██║   ██║██╔██╗ ██║██║  ███╗')
    console.gotoxy(50,8)
    print('██║╚██╔╝██║██╔══██║██╔══██║██   ██║██║   ██║██║╚██╗██║██║   ██')
    console.gotoxy(50,9)
    print('██║ ╚═╝ ██║██║  ██║██║  ██║╚█████╔╝╚██████╔╝██║ ╚████║╚██████╔╝')
    console.gotoxy(50,10)
    print('╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚════╝  ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝')

def printDificuldadeTitle():
    console.gotoxy(43,5)
    print('██████╗ ██╗███████╗██╗ ██████╗██╗   ██╗██╗     ██████╗  █████╗ ██████╗ ███████╗')
    console.gotoxy(43,6)
    print('██╔══██╗██║██╔════╝██║██╔════╝██║   ██║██║     ██╔══██╗██╔══██╗██╔══██╗██╔════╝')
    console.gotoxy(43,7)
    print('██║  ██║██║█████╗  ██║██║     ██║   ██║██║     ██║  ██║███████║██║  ██║█████╗  ')
    console.gotoxy(43,8)
    print('██║  ██║██║██╔══╝  ██║██║     ██║   ██║██║     ██║  ██║██╔══██║██║  ██║██╔══╝  ')
    console.gotoxy(43,9)
    print('██████╔╝██║██║     ██║╚██████╗╚██████╔╝███████╗██████╔╝██║  ██║██████╔╝███████╗')
    console.gotoxy(43,10)
    print('╚═════╝ ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝')

def printRankingTitle():
    console.gotoxy(50,5)
    print('██████╗  █████╗ ███╗   ██╗██╗  ██╗██╗███╗   ██╗ ██████╗ ')
    console.gotoxy(50,6)
    print('██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝██║████╗  ██║██╔════╝ ')
    console.gotoxy(50,7)
    print('██████╔╝███████║██╔██╗ ██║█████╔╝ ██║██╔██╗ ██║██║  ███╗')
    console.gotoxy(50,8)
    print('██╔══██╗██╔══██║██║╚██╗██║██╔═██╗ ██║██║╚██╗██║██║   ██║')
    console.gotoxy(50,9)
    print('██║  ██║██║  ██║██║ ╚████║██║  ██╗██║██║ ╚████║╚██████╔╝')
    console.gotoxy(50,10)
    print('╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ')

def printPointsTittle():
    console.gotoxy(50,5)
    print('\033[1;34;40m' + '   _ \   ____|   ___|   |   |   \  |   _ \     ')
    console.gotoxy(50,6)
    print('  |   |  __|   \___ \   |   |  |\/ |  |   | _) ')
    console.gotoxy(50,7)
    print('  __ <   |           |  |   |  |   |  |   |    ')
    console.gotoxy(50,8)
    print(' _| \_\ _____| _____/  \___/  _|  _| \___/  _) ' + '\033[1;37;40m')

def printIntructionsTittle():
    console.gotoxy(55,5)
    print(' █████╗      ██╗██╗   ██╗██████╗  █████╗ ')
    console.gotoxy(55,6)
    print('██╔══██╗     ██║██║   ██║██╔══██╗██╔══██╗')
    console.gotoxy(55,7)
    print('███████║     ██║██║   ██║██║  ██║███████║')
    console.gotoxy(55,8)
    print('██╔══██║██   ██║██║   ██║██║  ██║██╔══██║')
    console.gotoxy(55,9)
    print('██║  ██║╚█████╔╝╚██████╔╝██████╔╝██║  ██║')
    console.gotoxy(55,10)
    print('╚═╝  ╚═╝ ╚════╝  ╚═════╝ ╚═════╝ ╚═╝  ╚═╝')


def printText(text, info, x, y):
    textSplit = text.split('/')
    for cont in range (0, len(textSplit)):
        console.gotoxy(x+cont, y)
        print(str(textSplit[cont]))
        sleep(0.12)
    sleep(0.5)
    console.gotoxy(x+len(textSplit)+1,y)
    print(str(info))

def printTime(time = 15):
    console.gotoxy(1,4)
    print('Tempo: ')
    console.gotoxy(1,3)
    print(chr(8254)*150)
    x = 10
    for cont in range(1, time+1):
        console.gotoxy(x, 4)
        print(cont)
        x += 10

def printMenuStyle(heitgh = 30):
    printBarras(heitgh)
    printMenuTitle()

def printDificuldadeStyle(heitgh = 30):
    printBarras(heitgh)
    printDificuldadeTitle()

def printGamestyle(heitgh = 30):
    printBarras(heitgh)
    printTime()

def printRankingStyle(heitgh):
    printBarras(heitgh)
    printRankingTitle()

def printPointsStyle(heitgh = 30):
    printBarras(heitgh)
    printPointsTittle()

def printInstructionsStyle(heitgh = 50):
    printBarras(heitgh)
    printIntructionsTittle()
