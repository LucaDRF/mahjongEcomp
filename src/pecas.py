from random import choice
import src.modules.console as console

def printPeca(x, y, peca):

    console.gotoxy(x, y)

    print(chr(9487) + chr(9477)*3 + chr(9491))

    console.gotoxy(x, y+1)
    print(chr(9479) + '   ' + chr(9479))

    console.gotoxy(x, y+2)

    print(chr(9479) + ' '*3 + chr(9479)) 

    console.gotoxy(x, y+3)

    print(chr(9479) + '   ' + chr(9479))

    console.gotoxy(x, y+4)

    print(chr(9495) + chr(9477)*3 + chr(9498))  

    console.gotoxy(x+2, y+2)
    print(peca)

def randomizePecas():
    simbols = [63912, 63912, 63912, 63912, 63912, 63912, 12507, 12507, 12507, 12507, 131103, 131103, 131103, 131103,131220, 131220, 131220, 131220, 173863, 173863, 173863, 173863, 174117, 174117, 174117, 174117, 178151,178151, 178151, 178151, 194713, 194713, 194713, 194713, 194586, 194586, 194586, 194586]
    pecasPosition = [[0,0,1,1,1,1,1,0,0],
                     [0,1,1,1,1,1,1,1,0],
                     [0,1,1,1,1,1,1,1,0],
                     [0,1,1,1,1,1,1,1,0],
                     [0,1,1,1,1,1,1,1,0],
                     [0,0,1,1,1,1,1,0,0]]
    x = 60
    y = 8

    for contX in range(0, 9):
        for contY in range(0, 6):
            if (pecasPosition[contY][contX]):
                simbol = choice(simbols)
                printPeca(x + (contX * 5), y + (contY * 4), chr(simbol))
                pecasPosition[contY].insert(contX, str(simbol))
                simbols.remove(simbol)
                pecasPosition[contY].pop(contX + 1)
            
    return pecasPosition

def removePeca(matriz, matrizX, matrizY, currentX, currentY):
    matriz[matrizY].insert(matrizX, 0)
    matriz[matrizY].pop(matrizX + 1)
    matriz[currentY].insert(currentX, 0)
    matriz[currentY].pop(currentX + 1)

    x = 60
    y = 8

    for contY in range(0, len(matriz)):
        for contX in range(0, len(matriz[contY])):
            if (matriz[contY][contX]):
                printPeca(x + (contX * 5), y + (contY * 4), chr(int(matriz[contY][contX])))

    return matriz
