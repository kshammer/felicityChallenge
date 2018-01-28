heroInfo = {}
train9 = []
train1 = []
test1 = []
test9 = []

#reads the hero data and puts it in the dictionary heroInfo
def readHeroData():
    with open("../felicityChallenge/hero_data.csv") as data:
        lines = data.read().split('\n')[1:-1]
        for line in lines:
            tokens = line.split(',')
            heroInfo[tokens[0]] = []
            for x in range(1, 4):
                heroInfo[tokens[0]].append(tokens[x])
def readTrain9():
    with open("../felicityChallenge/train9.csv") as data:
        lines = data.read().split('\n')[1:]
        x = 0
        for line in lines:
            train9.append([])
            tokens = line.split(',')

            for token in tokens:
                train9[x].append(token)
            x += 1
def readTrain1():
    with open("../felicityChallenge/train1.csv") as data:
        lines = data.read().split('\n')[1:]
        x = 0
        for line in lines:
            train1.append([])
            tokens = line.split(',')

            for token in tokens:
                train1[x].append(token)
            x += 1
def readTest1():
    with open("../felicityChallenge/test1.csv") as data:
        lines = data.read().split('\n')[1:]
        x = 0
        for line in lines:
            test1.append([])
            tokens = line.split(',')

            for token in tokens:
                test1[x].append(token)
            x += 1
def readTest9():
    with open("../felicityChallenge/test9.csv") as data:
        lines = data.read().split('\n')[1:]
        x = 0
        for line in lines:
            test9.append([])
            tokens = line.split(',')

            for token in tokens:
                test9[x].append(token)
            x += 1


readHeroData()
readTrain9()
readTrain1()
readTest1()
readTest9()





