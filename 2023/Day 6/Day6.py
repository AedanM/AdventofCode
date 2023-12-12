import argparse


def createArray(arr):
    a = []
    for i in arr:
        if i.isnumeric():
            a.append(int(i))
    return a


def calcDistance(time, heldTime):
    return heldTime * (time - heldTime)


def pt1(filePath):
    with open(filePath, "r") as fp:
        timeArray = []
        winningArray = []
        distanceArray = []
        for line in fp:
            splitLine = line.replace("\n", "").split(" ")
            if "Time" in splitLine[0]:
                timeArray = createArray(splitLine)
            elif "Distance" in splitLine[0]:
                distanceArray = createArray(splitLine)
        for idx, time in enumerate(timeArray):
            currentRace = []
            for i in range(1, time):
                if calcDistance(time, i) > distanceArray[idx]:
                    currentRace.append(i)
            winningArray.append(currentRace)
        marginOfError = 1
        for i in winningArray:
            marginOfError *= len(i)
        print(marginOfError)


def pt2(filePath):
    with open(filePath, "r") as fp:
        timeArray = []
        winningArray = []
        distanceArray = []
        for line in fp:
            splitLine = line.replace("\n", "").replace(" ", "").split(":")
            if "Time" in splitLine[0]:
                timeArray = createArray(splitLine)
            elif "Distance" in splitLine[0]:
                distanceArray = createArray(splitLine)
        for idx, time in enumerate(timeArray):
            currentRace = []
            for i in range(1, time):
                if calcDistance(time, i) > distanceArray[idx]:
                    currentRace.append(i)
            winningArray.append(currentRace)
        marginOfError = 1
        for i in winningArray:
            marginOfError *= len(i)
        print(marginOfError)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="AOC Day6")
    parser.add_argument("-f", "--file", required="True")
    args = parser.parse_args()
    pt1(args.file)
    pt2(args.file)
