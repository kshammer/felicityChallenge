import matplotlib.pyplot as plt
import numpy as np
import csv
heroInfo = {}
train9 = []
train1 = []
test1 = []
test9 = []
#delete less than 10 games


def plotratiovskda():
    x = []
    y = []
    for players in train9:
        x.append(float(players[4])/(float(players[3])))
        y.append(players[5])
    plt.scatter(x, y)
    plt.show()
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
        if float(player[5]) < min:
            min = float(player[5])
        if float(player[5]) > max:
            max = float(player[5])
    bottom = max - min
    print(min)
    print(max)
    for player in train9:
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
    y1 = []
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

    with open("herovKDA.csv", "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        cool = zip(z, y1)
        for val in cool:
            writer.writerow(val)


def plotwinratioperplayer():
    x = []
    y = []
    y1 = []
    for z in range(1, 2993):
        y.append([])
    for player in train9:
        y[int(player[0]) - 1].append(float(player[4])/float(player[3]))
    for sub in y:
        if len(sub) > 0:
            y1.append(np.mean(sub))
    x = list(range(1, len(y1) + 1))
    z = [x for _, x in sorted(zip(y1, x))]
    y1 = sorted(y1)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(x, y1)
   # plt.show()
    with open("playervsratio.csv", "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        cool = zip(z, y1)
        for val in cool:
            writer.writerow(val)


def addSkillTrain9():
    x = []
    y = []
    y1 = []
    for z in range(1, 2993):
        y.append([])
    for player in train9:
        y[int(player[0]) - 1].append(float(player[4]) / float(player[3]))
    u = 1
    for sub in y:
        if len(sub) > 0:
            y1.append(np.mean(sub))
            x.append(u)
        else:
            print("ez")
        u += 1

    with open("train9.csv", 'a', newline='') as f:
        writer = csv.writer(f)
        cool = zip(x, y1)
        for val in cool:
            writer.writerow(val)
def addSkillTest9():
    x = []
    y = []
    y1 = []
    for z in range(1, 2989):
        y.append([])
    for player in test9:
        y[int(player[0]) - 1].append(float(player[4]) / float(player[3]))
    u = 1
    for sub in y:
        if len(sub) > 0:
            y1.append(np.mean(sub))
            x.append(u)
        else:
            print("ez")
        u += 1

    with open("test9.csv", 'a', newline='') as f:
        writer = csv.writer(f)
        cool = zip(x, y1)
        for val in cool:
            writer.writerow(val)
def graphDataAverages():
    x = list(range(1,122))
    y = []
    y1 = []
    for z in range(1, 122):
        y.append([])
    for player in train9:
        y[int(player[1]) -1].append(float(player[5]))
    for sub in y:
        if len(sub) > 0:
            y1.append(np.mean(sub))
    #x = list(range(1, len(y1) + 1))
    z = [x for _, x in sorted(zip(y1,x))]
    print(z)
    y1 = sorted(y1)
def addKDAtoHeros():
    x = list(range(1, 122))
    y = []
    y1 = []
    for z in range(1, 122):
        y.append([])
    for player in train9:
        y[int(player[1]) - 1].append(float(player[5]))
    for player in test9:
        y[int(player[1]) - 1].append(float(player[5]))
    for sub in y:
        if len(sub) > 0:
            y1.append(np.mean(sub))
        else:
            y1.append(0)

    with open("hero_data.csv", 'a', newline='') as f:
        writer = csv.writer(f)
        cool = zip(x, y1)
        for val in cool:
            writer.writerow(val)








readHeroData()
readTrain9()
readTrain1()
readTest1()
readTest9()

addKDAtoHeros()
addSkillTrain9()
addSkillTest9()
#plotratiovskda()
#normalizeKDA()
#graphDataAverages()
#plotwinratioperplayer()
#23,114,115,116,117,120 never played






