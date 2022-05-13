import src.modules.console as console

def printBarras(heigth):
    console.gotoxy(1,1)
    print('\033[1;37;40m_'*150)

    console.gotoxy(1, heigth)
    print('\033[1;37;40m_'*150)

def printTitle():
    console.gotoxy(70,5)
    print('\033[1;31;40m='*15)

    console.gotoxy(70,7)
    print('\033[1;31;40m='*15)

def printStyle(heigth = 30):
    printBarras(heigth)
    printTitle()