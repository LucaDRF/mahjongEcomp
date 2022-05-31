from time import sleep
import src.modules.console as console
import src.modules.keyboard as keyboard
import src.style as style
import src.dificuldade as dificuldade
import src.ranking as ranking

def quitGame():
    console.reset(1, 1, 30, 150)
    quit()

def execute():
    printMenu()
    selectItem()

def printMenu():
    console.init(30)
    console.reset(1,1,30,150)

    sleep(0.5)

    console.gotoxy(40, 15)
    print('\033[1;36;40m' + chr(9487) + chr(9477)*15 + chr(9491))
    console.gotoxy(40, 16)
    print(chr(9479) + ' '*15 + chr(9479))
    console.gotoxy(40, 17)
    print(chr(9479) + '     Jogar     ' + chr(9479))
    console.gotoxy(40, 18)
    print(chr(9479) + ' '*15 + chr(9479))
    console.gotoxy(40, 19)
    print(chr(9495) + chr(9477)*15 + chr(9498))

    console.gotoxy(70, 15)
    print(chr(9487) + chr(9477)*15 + chr(9491))
    console.gotoxy(70, 16)
    print(chr(9479) + ' '*15 + chr(9479))
    console.gotoxy(70, 17)
    print(chr(9479) + '    Ranking    ' + chr(9479))
    console.gotoxy(70, 18)
    print(chr(9479) + ' '*15 + chr(9479))
    console.gotoxy(70, 19)
    print(chr(9495) + chr(9477)*15 + chr(9498))

    console.gotoxy(100, 15)
    print(chr(9487) + chr(9477)*15 + chr(9491))
    console.gotoxy(100, 16)
    print(chr(9479) + ' '*15 + chr(9479))
    console.gotoxy(100, 17)
    print(chr(9479) + '      Sair     ' + chr(9479))
    console.gotoxy(100, 18)
    print(chr(9479) + ' '*15 + chr(9479))
    console.gotoxy(100, 19)
    print(chr(9495) + chr(9477)*15 + chr(9498))

    style.printMenuStyle()
    console.gotoxy(48,17)

def selectItem():
    keySelected = ['jogar','ranking', 'sair']
    functions = {'jogar': dificuldade.printDificuldade, 'ranking': ranking.printRanking, 'sair': quitGame}
    position = 0
    x = 48
    y = 17

    while True:
        event = keyboard.read_event()

        if(event.event_type == keyboard.KEY_DOWN):
            if(event.name == 'right' and position < 2):
                position += 1
                x += 30

            elif (event.name == 'left' and position > 0):
                position -= 1
                x -= 30

            elif (event.name == 'esc'):
                quitGame()

            elif (event.name == 'enter'):
                console.reset(1, 1, 30, 150)

                functions[keySelected[position]]()

                printMenu()

        console.gotoxy(x, y)
