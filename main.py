import matplotlib.pyplot as plt
import numpy as np
heroInfo = {}
train9 = []
train1 = []
test1 = []
test9 = []
#delete less than 10 games

#reads the hero data and puts it in the dictionary heroInfo
def readHeroData():
    with open("../felicityChallenge/hero_data.csv") as data:
        lines = data.read().split('\n')[1:-1]#remove first and last entry
        for line in lines:
            tokens = line.split(',')
            heroInfo[tokens[0]] = []
            for x in range(1, 4):
                heroInfo[tokens[0]].append(tokens[x])
def readTrain9():
    with open("../felicityChallenge/train9.csv") as data:
        lines = data.read().split('\n')[1:-1]
        x = 0
        for line in lines:
            train9.append([])
            tokens = line.split(',')

            for token in tokens:
                train9[x].append(token)
            x += 1
def readTrain1():
    with open("../felicityChallenge/train1.csv") as data:
        lines = data.read().split('\n')[1:-1]
        x = 0
        for line in lines:
            train1.append([])
            tokens = line.split(',')

            for token in tokens:
                train1[x].append(token)
            x += 1
def readTest1():
    with open("../felicityChallenge/test1.csv") as data:
        lines = data.read().split('\n')[1:-1]
        x = 0
        for line in lines:
            test1.append([])
            tokens = line.split(',')

            for token in tokens:
                test1[x].append(token)
            x += 1
def readTest9():
    with open("../felicityChallenge/test9.csv") as data:
        lines = data.read().split('\n')[1:-1]
        x = 0
        for line in lines:
            test9.append([])
            tokens = line.split(',')

            for token in tokens:
                test9[x].append(token)
            x += 1
def normalizeKDA():
    min = 999999.0
    max = 0.0
    for player in train9:
        if int(player[3]) > 10:
            if float(player[5]) < min:
                min = float(player[5])
            if float(player[5]) > max:
                max = float(player[5])
    bottom = max - min
    for player in train9:
        if int(player[3]) > 10:
            top = float(player[5]) - min
            player.append(top/bottom)


def graphData():
    x = []
    y = []
    for z in range(1,122):
        y.append([])
    for player in train9:
        x.append(player[1])
        y[int(player[1])-1].append(player[5])
    for xe, ye in zip(x, y):
        plt.scatter([xe] * len(ye), ye)
    plt.show()
def graphDataNormal():
    x = []
    y = []
    #adding emtpy arrays
    for z in range(1, 122):
        y.append([])
    for player in train9:
        x.append(player[1])
        if len(player) == 7:
            y[int(player[1]) - 1].append(player[6])
    for xe, ye in zip(x, y):
        plt.scatter([xe] * len(ye), ye)
    plt.show()



readHeroData()
readTrain9()
readTrain1()
readTest1()
readTest9()
normalizeKDA()
graphDataNormal()






