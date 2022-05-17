from math import floor
from time import sleep
import src.modules.console as console
import src.style as style


def countdown(timePassed):
    times = floor(timePassed / 6)
    x = 1
    y = 2

    for cont in range(0, times):
        console.gotoxy(x * cont, y)
        print('\033[1;31;40m' + chr(9608) + '\033[1;37;40m')
