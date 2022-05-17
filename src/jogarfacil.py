from time import sleep, time
import src.pecas as pecas
import src.modules.console as console
import src.modules.keyboard as keyboard
import src.style as style
import src.timer as timer

def printGame():
    console.init(30)
    console.reset(1,1,30,150)
    style.printGamestyle()
    pecas.randomizePecas()

    firstTime = time()

    while True:
        currentTime = time()
        keyboard.read_event()

        timer.countdown(currentTime - firstTime)

        if (currentTime - firstTime) / 60 >= 15:
            console.reset(1,1,30,150)
            print('TEMPO ACABOU!')
            sleep(10)
            break

