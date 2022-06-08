from time import sleep
import src.modules.console as console
import src.modules.keyboard as keyboard
import src.style as style
import src.dificuldade as dificuldade
import src.ranking as ranking
import src.utils as utils
import src.intructions as instructions

def getName():
    name = input('Digite seu Nome: ')
    utils.name = name

def execute():
    getName()
    printMenu()
    selectItem()

def printMenu():
    console.init(30)
    console.reset(1,1,30,150)

    sleep(0.5)

    console.gotoxy(30, 15)
    print('\033[1;36;40m' + chr(9487) + chr(9473)*15 + chr(9491))
    console.gotoxy(30, 16)
    print(chr(9475) + ' '*15 + chr(9475))
    console.gotoxy(30, 17)
    print(chr(9475) + '     Jogar     ' + chr(9475))
    console.gotoxy(30, 18)
    print(chr(9475) + ' '*15 + chr(9475))
    console.gotoxy(30, 19)
    print(chr(9495) + chr(9473)*15 + chr(9499))

    console.gotoxy(60, 15)
    print(chr(9487) + chr(9473)*15 + chr(9491))
    console.gotoxy(60, 16)
    print(chr(9475) + ' '*15 + chr(9475))
    console.gotoxy(60, 17)
    print(chr(9475) + '    Ranking    ' + chr(9475))
    console.gotoxy(60, 18)
    print(chr(9475) + ' '*15 + chr(9475))
    console.gotoxy(60, 19)
    print(chr(9495) + chr(9473)*15 + chr(9499))
    
    console.gotoxy(90, 15)
    print(chr(9487) + chr(9473)*15 + chr(9491))
    console.gotoxy(90, 16)
    print(chr(9475) + ' '*15 + chr(9475))
    console.gotoxy(90, 17)
    print(chr(9475) + '     Ajuda     ' + chr(9475))
    console.gotoxy(90, 18)
    print(chr(9475) + ' '*15 + chr(9475))
    console.gotoxy(90, 19)
    print(chr(9495) + chr(9473)*15 + chr(9499))
    
    console.gotoxy(120, 15)
    print(chr(9487) + chr(9473)*15 + chr(9491))
    console.gotoxy(120, 16)
    print(chr(9475) + ' '*15 + chr(9475))
    console.gotoxy(120, 17)
    print(chr(9475) + '      Sair     ' + chr(9475))
    console.gotoxy(120, 18)
    print(chr(9475) + ' '*15 + chr(9475))
    console.gotoxy(120, 19)
    print(chr(9495) + chr(9473)*15 + chr(9499))



    style.printMenuStyle()
    console.gotoxy(38,17)

def selectItem():
    keySelected = ['jogar','ranking', 'instruções', 'sair']
    functions = {'jogar': dificuldade.printDificuldade, 'ranking': ranking.printRanking, 'instruções':instructions.printInstructions,'sair': utils.quitGame}
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

            elif (event.name == 'esc'):
                utils.quitGame()

            elif (event.name == 'enter'):
                console.reset(1, 1, 30, 150)

                functions[keySelected[position]]()

                printMenu()

        console.gotoxy(x, y)
