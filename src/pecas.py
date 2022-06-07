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
                pecasPosition[contY][contX] = str(simbol)
                simbols.remove(simbol)

    return pecasPosition

def randomizeMediumPecas():
    simbols = [63912, 63912, 63912, 63912, 63912, 63912, 12507, 12507, 12507, 12507, 131103, 131103, 131103, 131103,131220, 131220, 131220, 131220, 173863, 173863, 173863, 173863, 174117, 174117, 174117, 174117, 178151,178151, 178151, 178151, 194713, 194713, 194713, 194713, 194586, 194586, 194586, 194586, 63912, 63912, 63912, 63912, 63912, 63912, 12507, 12507, 12507, 12507, 131103, 131103, 131103, 131103,131220, 131220, 131220, 131220, 173863, 173863, 173863, 173863, 174117, 174117, 174117, 174117, 178151,178151, 178151, 178151, 194713, 194713, 194713, 194713, 194586, 194586, 194586, 194586, 63912, 63912, 63912, 63912, 63912, 63912, 12507, 12507, 12507, 12507, 131103, 131103, 131103, 131103,131220, 131220, 131220, 131220, 173863, 173863, 173863, 173863, 174117, 174117, 174117, 174117, 178151,178151, 178151, 178151, 194713, 194713, 194713, 194713, 194586, 194586]
    pecasPositionLayer1 = [[0,0,1,1,1,1,1,1,1,0,0],
                           [0,1,1,1,1,1,1,1,1,1,0],
                           [0,1,1,1,1,1,1,1,1,1,0],
                           [0,1,1,1,1,1,1,1,1,1,0],
                           [0,1,1,1,1,1,1,1,1,1,0],
                           [0,1,1,1,1,1,1,1,1,1,0],
                           [0,1,1,1,1,1,1,1,1,1,0],
                           [0,0,1,1,1,1,1,1,1,0,0]]   #68 pecas

    pecasPositionLayer2 = [[0,0,0,0,1,1,1,0,0,0,0],
                           [0,0,0,1,1,1,1,1,0,0,0],
                           [0,0,1,1,1,1,1,1,1,0,0],
                           [0,0,1,1,1,1,1,1,1,0,0],
                           [0,0,1,1,1,1,1,1,1,0,0],
                           [0,0,1,1,1,1,1,1,1,0,0],
                           [0,0,0,1,1,1,1,1,0,0,0],
                           [0,0,0,0,1,1,1,0,0,0,0]]   #44 pecas    total=112   simbols=2x9    6 per type and two types with 8

    x = 60
    y = 8

    for contX in range(0, 11):
        for contY in range(0, 8):
            if (pecasPositionLayer1[contY][contX]):
                simbol = choice(simbols)
                printPeca(x + (contX * 5), y + (contY * 4), chr(simbol))
                pecasPositionLayer1[contY][contX] = str(simbol)
                simbols.remove(simbol)

    for contX in range(0, 11):
        for contY in range(0, 8):
            if (pecasPositionLayer2[contY][contX]):
                simbol = choice(simbols)
                printPeca(x + (contX * 5) - 1, y + (contY * 4) - 1, chr(simbol))
                pecasPositionLayer2[contY][contX] = str(simbol)
                simbols.remove(simbol)

    return [pecasPositionLayer1, pecasPositionLayer2]

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

def removePecaTrid(matrizTrid, matrizX, matrizY, matrizIsLevelOne, currentX, currentY, currentIsLevelOne):
    if (currentIsLevelOne):
        matrizTrid[0][currentY].insert(currentX, 0)
        matrizTrid[0][currentY].pop(currentX + 1)
    else:
        matrizTrid[1][currentY].insert(currentX, 0)
        matrizTrid[1][currentY].pop(currentX + 1)

    if (matrizIsLevelOne):
        matrizTrid[0][matrizY].insert(matrizX, 0)
        matrizTrid[0][matrizY].pop(matrizX + 1)
    else:
        matrizTrid[1][matrizY].insert(matrizX, 0)
        matrizTrid[1][matrizY].pop(matrizX + 1)

    x = 60
    y = 8

    for contY in range(0, len(matrizTrid[0])):
        for contX in range(0, len(matrizTrid[0][contY])):
            if (matrizTrid[0][contY][contX]):
                printPeca(x + (contX * 5), y + (contY * 4), chr(int(matrizTrid[0][contY][contX])))

    for contY in range(0, len(matrizTrid[1])):
        for contX in range(0, len(matrizTrid[1][contY])):
            if (matrizTrid[1][contY][contX]):
                printPeca(x + (contX * 5) - 1, y + (contY * 4) - 1, chr(int(matrizTrid[1][contY][contX])))

    return matrizTrid
