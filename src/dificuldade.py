from time import sleep
import src.modules.console as console
import src.modules.keyboard as keyboard
import src.style as style

def printMenu():
    console.init(30)
    console.reset(1, 1, 30, 120)

    sleep(0.5)
    
    console.gotoxy(30, 15)
    print('\033[1;32;40m' + chr(9487) + chr(9477)*15 + chr(9491))
    console.gotoxy(30, 16)
    print(chr(9479) + ' '*15 + chr(9479))
    console.gotoxy(30, 17)
    print(chr(9479) + '     Fácil     ' + chr(9479))
    console.gotoxy(30, 18)
    print(chr(9479) + ' '*15 + chr(9479))
    console.gotoxy(30, 19)
    print(chr(9495) + chr(9477)*15 + chr(9498))

    console.gotoxy(60, 15)
    print('\033[1;33;40m' + chr(9487) + chr(9477)*15 + chr(9491))
    console.gotoxy(60, 16)
    print(chr(9479) + ' '*15 + chr(9479))
    console.gotoxy(60, 17)
    print(chr(9479) + '     Médio     ' + chr(9479))
    console.gotoxy(60, 18)
    print(chr(9479) + ' '*15 + chr(9479))
    console.gotoxy(60, 19)
    print(chr(9495) + chr(9477)*15 + chr(9498))
    
    console.gotoxy(90, 15)
    print('\033[1;31;40m' + chr(9487) + chr(9477)*15 + chr(9491))
    console.gotoxy(90, 16)
    print(chr(9479) + ' '*15 + chr(9479))
    console.gotoxy(90, 17)
    print(chr(9479) + '    Díficil    ' + chr(9479))
    console.gotoxy(90, 18)
    print(chr(9479) + ' '*15 + chr(9479))
    console.gotoxy(90, 19)
    print(chr(9495) + chr(9477)*15 + chr(9498))

    console.gotoxy(120, 15)
    print('\033[1;34;40m' + chr(9487) + chr(9477)*15 + chr(9491))
    console.gotoxy(120, 16)
    print(chr(9479) + ' '*15 + chr(9479))
    console.gotoxy(120, 17)
    print(chr(9479) + '     Voltar    ' + chr(9479))
    console.gotoxy(120, 18)
    print(chr(9479) + ' '*15 + chr(9479))
    console.gotoxy(120, 19)
    print(chr(9495) + chr(9477)*15 + chr(9498))

    style.printStyle()
    console.gotoxy(72, 6)
    print('\033[1;35;40mDIFICULDADE')
    console.gotoxy(31,15)


def selectItem():
    keySelected = ['facil', 'facil', 'medio', 'medio', 'difcil', 'dificil', 'voltar', 'voltar']
    position = 0
    x = 31
    y = 15

    while True:
        keyPressed = keyboard.read_key()

        if(keyPressed == 'right' and position < 6):
            position += 1
            x += 15

        elif (keyPressed == 'left' and position > 0):
            position -= 1
            x -= 15

        elif (keyPressed == 'enter'):
            console.reset(1,1,30,120)
            break

        console.gotoxy(x, y)


def printDificuldade():
    printMenu()
    selectItem()
