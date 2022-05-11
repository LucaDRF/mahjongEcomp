import src.modules.console as console

def printBarras():
    console.gotoxy(1,1)
    print('_'*150)

    console.gotoxy(1,30)
    print('_'*150)

def printTitle():
    console.gotoxy(70,5)
    print('\033[1;31;40m='*15)
    
    console.gotoxy(70,7)
    print('\033[1;31;40m='*15)

def printStyle():
    printBarras()
    printTitle()