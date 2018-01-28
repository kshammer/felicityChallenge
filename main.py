heroInfo = {}

#reads the hero data and puts it in the dictionary heroInfo
def readHeroData():
    with open("../felicityChallenge/hero_data.csv") as data:
        lines = data.read().split('\n')[1:-1]
        for line in lines:
            tokens = line.split(',')
            heroInfo[tokens[0]] = []
            for x in range(1, 4):
                heroInfo[tokens[0]].append(tokens[x])
readHeroData()




