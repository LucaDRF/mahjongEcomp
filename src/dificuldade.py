from time import sleep
import src.modules.console as console
import src.modules.keyboard as keyboard
import src.style as style
import src.play as play
import src.menu as menu

def printMenu():
    console.init(30)
    console.reset(1, 1, 30, 150)

    sleep(0.5)

    console.gotoxy(30, 15)
    print('\033[1;32;40m' + chr(9487) + chr(9473)*15 + chr(9491))
    console.gotoxy(30, 16)
    print(chr(9475) + ' '*15 + chr(9475))
    console.gotoxy(30, 17)
    print(chr(9475) + '     Fácil     ' + chr(9475))
    console.gotoxy(30, 18)
    print(chr(9475) + ' '*15 + chr(9475))
    console.gotoxy(30, 19)
    print(chr(9495) + chr(9473)*15 + chr(9499))

    console.gotoxy(60, 15)
    print('\033[1;33;40m' + chr(9487) + chr(9473)*15 + chr(9491))
    console.gotoxy(60, 16)
    print(chr(9475) + ' '*15 + chr(9475))
    console.gotoxy(60, 17)
    print(chr(9475) + '     Médio     ' + chr(9475))
    console.gotoxy(60, 18)
    print(chr(9475) + ' '*15 + chr(9475))
    console.gotoxy(60, 19)
    print(chr(9495) + chr(9473)*15 + chr(9499))

    console.gotoxy(90, 15)
    print('\033[1;31;40m' + chr(9487) + chr(9473)*15 + chr(9491))
    console.gotoxy(90, 16)
    print(chr(9475) + ' '*15 + chr(9475))
    console.gotoxy(90, 17)
    print(chr(9475) + '    Díficil    ' + chr(9475))
    console.gotoxy(90, 18)
    print(chr(9475) + ' '*15 + chr(9475))
    console.gotoxy(90, 19)
    print(chr(9495) + chr(9473)*15 + chr(9499))

    console.gotoxy(120, 15)
    print('\033[1;34;40m' + chr(9487) + chr(9473)*15 + chr(9491))
    console.gotoxy(120, 16)
    print(chr(9475) + ' '*15 + chr(9475))
    console.gotoxy(120, 17)
    print(chr(9475) + '     Voltar    ' + chr(9475))
    console.gotoxy(120, 18)
    print(chr(9475) + ' '*15 + chr(9475))
    console.gotoxy(120, 19)
    print(chr(9495) + chr(9473)*15 + chr(9499))

    style.printDificuldadeStyle()
    console.gotoxy(38,17)


def selectItem():
    keySelected = ['facil', 'medio', 'dificil', 'voltar']
    functions = {'facil':play.printGameEasy, 'medio':play.printGameMedium, 'dificil': play.printGameHard, 'voltar':menu.execute}
    position = 0
    x = 38
    y = 17

    while True:
        event = keyboard.read_event()

        if(event.event_type == keyboard.KEY_DOWN):
            if(event.name == 'right' and position < 3):
                position += 1
                x += 30
            elif (event.name == 'left' and position > 0):
                position -= 1
                x -= 30

            elif (event.name == 'enter'):
                console.reset(1, 1, 30, 150)
                functions[keySelected[position]]()
                break

        console.gotoxy(x, y)

def printDificuldade():
    printMenu()
    selectItem()
