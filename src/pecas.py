from random import choice
import src.modules.console as console

def printPeca(x, y, peca, colour):

    console.gotoxy(x, y)

    print(colour + chr(9487) + chr(9477)*3 + chr(9491))

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
    simbols = [36,36,36,36,36,36,38,38,38,38,42,42,42,42,43,43,43,43,64,64,64,64,165,165,165,165,198,198,198,198,248,248,248,248,426,426,426,426]
    pecasPosition = [[0,0,1,1,1,1,1,0,0],
                     [0,1,1,1,1,1,1,1,0],
                     [0,1,1,1,1,1,1,1,0],
                     [0,1,1,1,1,1,1,1,0],
                     [0,1,1,1,1,1,1,1,0],
                     [0,0,1,1,1,1,1,0,0]] #38 pecas 9 simbols  9x4+2
    x = 60
    y = 8

    for contX in range(0, 9):
        for contY in range(0, 6):
            if (pecasPosition[contY][contX]):
                simbol = choice(simbols)
                printPeca(x + (contX * 5), y + (contY * 4), chr(simbol), '\033[1;37;40m')
                pecasPosition[contY][contX] = str(simbol)
                simbols.remove(simbol)

    return pecasPosition

def randomizeMediumPecas():
    simbols = [36,36,36,36,36,36,38,38,38,38,38,36,42,42,42,42,42,42,43,43,43,43,43,43,64,64,64,64,64,64,165,165,165,165,165,165,198,198,198,198,198,198,248,248,248,248,248,248,426,
    426,426,426,426,426,440,440,440,440,440,440,586,586,586,586,586,586,622,622,622,622,622,622,677,677,677,677,677,677,936,936,936,936,936,936,1288,1288,1288,1288,1288,1288,1069,
    1069,1069,1069,1069,1069,684,684,684,684,684,684,882,882,882,882,882,882,882,882]
    pecasPositionLayer1 = [[0,0,1,1,1,1,1,1,1,0,0],
                           [0,1,1,1,1,1,1,1,1,1,0],
                           [0,1,1,1,1,1,1,1,1,1,0],
                           [0,1,1,1,1,1,1,1,1,1,0],
                           [0,1,1,1,1,1,1,1,1,1,0],
                           [0,1,1,1,1,1,1,1,1,1,0],
                           [0,1,1,1,1,1,1,1,1,1,0],
                           [0,0,1,1,1,1,1,1,1,0,0]]   #68 pecas

    pecasPositionLayer2 = [[0,0,0,0,0,0,0,0,0,0,0],
                           [0,0,1,1,1,1,1,1,1,0,0],
                           [0,0,1,1,1,1,1,1,1,0,0],
                           [0,0,1,1,1,1,1,1,1,0,0],
                           [0,0,1,1,1,1,1,1,1,0,0],
                           [0,0,1,1,1,1,1,1,1,0,0],
                           [0,0,1,1,1,1,1,1,1,0,0],
                           [0,0,0,0,0,0,0,0,0,0,0]]   #42 pecas    total=110   simbols=2x9    6 per type and one type with 8

    x = 60
    y = 8

    for contX in range(0, 11):
        for contY in range(0, 8):
            if (pecasPositionLayer1[contY][contX]):
                simbol = choice(simbols)
                printPeca(x + (contX * 5), y + (contY * 4), chr(simbol), '\033[1;37;40m')
                pecasPositionLayer1[contY][contX] = str(simbol)
                simbols.remove(simbol)

    for contX in range(0, 11):
        for contY in range(0, 8):
            if (pecasPositionLayer2[contY][contX]):
                simbol = choice(simbols)
                printPeca(x + (contX * 5), y + (contY * 4), chr(simbol), '\033[1;34;40m')
                pecasPositionLayer2[contY][contX] = str(simbol)
                simbols.remove(simbol)

    return [pecasPositionLayer1, pecasPositionLayer2]

def randomizeHardPecas():
    simbols = [36,36,36,36,36,36,38,38,38,38,38,38,42,42,42,42,42,42,43,43,43,43,43,43,64,64,64,64,64,64,165,165,165,165,165,165,198,198,198,198,198,198,248,248,248,248,248,248,426,426,426,
    426,426,426,440,440,440,440,440,440,586,586,586,586,586,586,622,622,622,622,622,622,677,677,677,677,677,677,936,936,936,936,936,936,1288,1288,1288,1288,1288,1288,1069,1069,1069,
    1069,1069,1069,684,684,684,684,684,684,882,882,882,882,882,882,9827,9827,9827,9827,9827,9827,9829,9829,9829,9829,9830,9830,9830,9830,9824,9824,9824,9824,9834,9834,9834,9834,9835,
    9835,9835,9835,9650,9650,9650,9650,404,404,404,404,911,911,911,911]
    pecasPositionLayer1 = [[0,0,1,1,1,1,1,1,1,0,0],
                           [0,1,1,1,1,1,1,1,1,1,0],
                           [0,1,1,1,1,1,1,1,1,1,0],
                           [0,1,1,1,1,1,1,1,1,1,0],
                           [0,1,1,1,1,1,1,1,1,1,0],
                           [0,1,1,1,1,1,1,1,1,1,0],
                           [0,1,1,1,1,1,1,1,1,1,0],
                           [0,0,1,1,1,1,1,1,1,0,0]]   #68 pecas

    pecasPositionLayer2 = [[0,0,1,1,1,1,1,1,1,0,0],
                           [0,0,0,1,1,1,1,1,0,0,0],
                           [0,0,1,1,1,1,1,1,1,0,0],
                           [0,0,1,1,1,1,1,1,1,0,0],
                           [0,0,1,1,1,1,1,1,1,0,0],
                           [0,0,1,1,1,1,1,1,1,0,0],
                           [0,0,0,1,1,1,1,1,0,0,0],
                           [0,0,1,1,1,1,1,1,1,0,0]]   #52 pecas    total=112   simbols=2x9    6 per type and two types with 8

    pecasPositionLayer3 = [[0,0,0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,1,1,1,0,0,0,0],
                           [0,0,0,1,1,1,1,1,0,0,0],
                           [0,0,0,1,1,1,1,1,0,0,0],
                           [0,0,0,1,1,1,1,1,0,0,0],
                           [0,0,0,1,1,1,1,1,0,0,0],
                           [0,0,0,0,1,1,1,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0,0,0]]   #26 pecas total = 146 3x9 19 with 6 and 10 with 4

    x = 60
    y = 8

    for contX in range(0, 11):
        for contY in range(0, 8):
            if (pecasPositionLayer1[contY][contX]):
                simbol = choice(simbols)
                printPeca(x + (contX * 5), y + (contY * 4), chr(simbol), '\033[1;37;40m')
                pecasPositionLayer1[contY][contX] = str(simbol)
                simbols.remove(simbol)

    for contX in range(0, 11):
        for contY in range(0, 8):
            if (pecasPositionLayer2[contY][contX]):
                simbol = choice(simbols)
                printPeca(x + (contX * 5), y + (contY * 4), chr(simbol), '\033[1;34;40m')
                pecasPositionLayer2[contY][contX] = str(simbol)
                simbols.remove(simbol)

    for contX in range(0, 11):
        for contY in range(0, 8):
            if (pecasPositionLayer3[contY][contX]):
                simbol = choice(simbols)
                printPeca(x + (contX * 5), y + (contY * 4), chr(simbol), '\033[1;32;40m')
                pecasPositionLayer3[contY][contX] = str(simbol)
                simbols.remove(simbol)

    return [pecasPositionLayer1, pecasPositionLayer2, pecasPositionLayer3]

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
                printPeca(x + (contX * 5), y + (contY * 4), chr(int(matriz[contY][contX])), '\033[1;37;40m')

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
                printPeca(x + (contX * 5), y + (contY * 4), chr(int(matrizTrid[0][contY][contX])), '\033[1;37;40m')

    for contY in range(0, len(matrizTrid[1])):
        for contX in range(0, len(matrizTrid[1][contY])):
            if (matrizTrid[1][contY][contX]):
                printPeca(x + (contX * 5), y + (contY * 4), chr(int(matrizTrid[1][contY][contX])), '\033[1;34;40m')

    return matrizTrid

def removePecaTridHard(matrizTrid, matrizX, matrizY, matrizIsLevelOne, matrizIsLevelTwo, currentX, currentY, currentIsLevelOne, currentIsLevelTwo):
    if (currentIsLevelOne):
        matrizTrid[0][currentY].insert(currentX, 0)
        matrizTrid[0][currentY].pop(currentX + 1)
    elif (currentIsLevelTwo):
        matrizTrid[1][currentY].insert(currentX, 0)
        matrizTrid[1][currentY].pop(currentX + 1)
    else:
        matrizTrid[2][currentY].insert(currentX, 0)
        matrizTrid[2][currentY].pop(currentX + 1)

    if (matrizIsLevelOne):
        matrizTrid[0][matrizY].insert(matrizX, 0)
        matrizTrid[0][matrizY].pop(matrizX + 1)
    elif (matrizIsLevelTwo):
        matrizTrid[1][matrizY].insert(matrizX, 0)
        matrizTrid[1][matrizY].pop(matrizX + 1)
    else:
        matrizTrid[2][matrizY].insert(matrizX, 0)
        matrizTrid[2][matrizY].pop(matrizX + 1)

    x = 60
    y = 8

    for contY in range(0, len(matrizTrid[0])):
        for contX in range(0, len(matrizTrid[0][contY])):
            if (matrizTrid[0][contY][contX]):
                printPeca(x + (contX * 5), y + (contY * 4), chr(int(matrizTrid[0][contY][contX])), '\033[1;37;40m')

    for contY in range(0, len(matrizTrid[1])):
        for contX in range(0, len(matrizTrid[1][contY])):
            if (matrizTrid[1][contY][contX]):
                printPeca(x + (contX * 5), y + (contY * 4), chr(int(matrizTrid[1][contY][contX])), '\033[1;34;40m')

    for contY in range(0, len(matrizTrid[2])):
        for contX in range(0, len(matrizTrid[2][contY])):
            if (matrizTrid[2][contY][contX]):
                printPeca(x + (contX * 5), y + (contY * 4), chr(int(matrizTrid[2][contY][contX])), '\033[1;32;40m')

    return matrizTrid
