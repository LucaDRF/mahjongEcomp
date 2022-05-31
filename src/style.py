import src.modules.console as console

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
    console.gotoxy(40,5)
    print('██████╗ ██╗███████╗██╗ ██████╗██╗   ██╗██╗     ██████╗  █████╗ ██████╗ ███████╗')
    console.gotoxy(40,6)
    print('██╔══██╗██║██╔════╝██║██╔════╝██║   ██║██║     ██╔══██╗██╔══██╗██╔══██╗██╔════╝')
    console.gotoxy(40,7)
    print('██║  ██║██║█████╗  ██║██║     ██║   ██║██║     ██║  ██║███████║██║  ██║█████╗  ')
    console.gotoxy(40,8)
    print('██║  ██║██║██╔══╝  ██║██║     ██║   ██║██║     ██║  ██║██╔══██║██║  ██║██╔══╝  ')
    console.gotoxy(40,9)
    print('██████╔╝██║██║     ██║╚██████╗╚██████╔╝███████╗██████╔╝██║  ██║██████╔╝███████╗')
    console.gotoxy(40,10)
    print('╚═════╝ ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝')


def printTime(time = 15):
    console.gotoxy(1,4)
    print('Tempo: ')
    console.gotoxy(1,3)
    print(chr(8254)*150)
    x = 10
    for cont in range(1, 16):
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

def printRankingStyle(heitgh):
    printBarras(heitgh)
    printRankingTitle()