import src.modules.console as console
import src.modules.keyboard as keyboard

def execute():
    printMenu()
    selectItem()

def printMenu():
    console.init(30)

    console.reset(1,1,30,80)

    console.gotoxy(30, 15)
    print(chr(9487) + chr(9477)*15 + chr(9491))
    console.gotoxy(30, 16)
    print(chr(9479) + ' '*15 + chr(9479))
    console.gotoxy(30, 17)
    print(chr(9479) + '     Jogar     ' + chr(9479))
    console.gotoxy(30, 18)
    print(chr(9479) + ' '*15 + chr(9479))
    console.gotoxy(30, 19)
    print(chr(9495) + chr(9477)*15 + chr(9498))

    console.gotoxy(60, 15)
    print(chr(9487) + chr(9477)*15 + chr(9491))
    console.gotoxy(60, 16)
    print(chr(9479) + ' '*15 + chr(9479))
    console.gotoxy(60, 17)
    print(chr(9479) + '  Dificuldade  ' + chr(9479))
    console.gotoxy(60, 18)
    print(chr(9479) + ' '*15 + chr(9479))
    console.gotoxy(60, 19)
    print(chr(9495) + chr(9477)*15 + chr(9498))

    console.gotoxy(90, 15)
    print(chr(9487) + chr(9477)*15 + chr(9491))
    console.gotoxy(90, 16)
    print(chr(9479) + ' '*15 + chr(9479))
    console.gotoxy(90, 17)
    print(chr(9479) + '    Ranking    ' + chr(9479))
    console.gotoxy(90, 18)
    print(chr(9479) + ' '*15 + chr(9479))
    console.gotoxy(90, 19)
    print(chr(9495) + chr(9477)*15 + chr(9498))

    console.gotoxy(120, 15)
    print(chr(9487) + chr(9477)*15 + chr(9491))
    console.gotoxy(120, 16)
    print(chr(9479) + ' '*15 + chr(9479))
    console.gotoxy(120, 17)
    print(chr(9479) + '      Sair     ' + chr(9479))
    console.gotoxy(120, 18)
    print(chr(9479) + ' '*15 + chr(9479))
    console.gotoxy(120, 19)
    print(chr(9495) + chr(9477)*15 + chr(9498))

    console.gotoxy(31, 15)

def selectItem():
    keySelected = ['jogar', 'jogar', 'dificuldade', 'dificuldade', 'ranking', 'ranking', 'sair', 'sair']
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

        elif (keyPressed == 'esc'):
            console.reset(1,1,200,200)
            quit()

        elif (keyPressed == 'enter'):
            console.reset(1,1,200,200)
            print(keySelected[position])

        console.gotoxy(x, y)
