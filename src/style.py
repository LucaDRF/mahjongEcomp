import src.modules.console as console

def printBarras(heitgh):
    console.gotoxy(1,1)
    print('\033[1;37;40m_'*150)

    console.gotoxy(1,heitgh)
    print('\033[1;37;40m_'*150)

def printTitle():
    console.gotoxy(70,5)
    print('\033[1;31;40m='*15)
    
    console.gotoxy(70,7)
    print('\033[1;31;40m='*15)

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

def printStyle(heitgh = 30):
    printBarras(heitgh)
    printTitle()

def printGamestyle(heitgh = 30):
    printBarras(heitgh)
    printTime()

    

