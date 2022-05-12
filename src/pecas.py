import modules.console as console
console.init(30)
console.reset(1,1,30,120)

def printPecas(x, y, peca):

    console.gotoxy(x, y)

    print(chr(9487) + chr(9477)*3 + chr(9491))

    console.gotoxy(x, y+1)
    print(chr(9479) + '   ' + chr(9479))

    console.gotoxy(x, y+2)

    print(chr(9479) + ' ' + peca + ' ' + chr(9479)) 

    console.gotoxy(x, y+3)

    print(chr(9479) + '   ' + chr(9479))

    console.gotoxy(x, y+4)

    print(chr(9495) + chr(9477)*3 + chr(9498))  
