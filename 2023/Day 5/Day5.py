import argparse


def createMap(mapTomap, line):
    lineList = line.strip().split(" ")
    lineList = [int(i) for i in lineList]

    mapTomap.append(
        (lineList[1], lineList[1] + lineList[2], (-lineList[1] + lineList[0]))
    )


def checkMap(inputList, mapList):
    outputList = []

    for x in inputList:
        startLen = len(outputList)
        for mapEl in mapList:
            if x in range(mapEl[0], mapEl[1]):
                outputList.append(x + mapEl[2])
        if len(outputList) == startLen:
            outputList.append(x)
    return outputList


def createSeedList(line):
    slist = []
    slist = line.replace("seeds:", "").strip().split(" ")
    slist = [int(i) for i in slist]
    outList = []
    for i in range(0, len(slist)):
        print(i)
        try:
            if i % 2 == 0:
                outList.append(list(range(slist[i], slist[i] + slist[i + 1])))

        except:
            pass
    outList = sum(outList, [])
    return outList


def getCurrentMap(line, Mode):
    currentMap = ""
    if "seeds:" in line:
        currentMap = "seeds"
    elif "to-soil" in line:
        currentMap = "soil"
    elif "to-fertilizer" in line:
        currentMap = "fertilizer"
    elif "to-water" in line:
        currentMap = "water"
    elif "to-light" in line:
        currentMap = "light"
    elif "to-temperature" in line:
        currentMap = "temperature"
    elif "to-humidity" in line:
        currentMap = "humidity"
    elif "to-location" in line:
        currentMap = "location"
    else:
        currentMap = Mode
    return currentMap


def pt2(filePath):
    with open(filePath, "r") as fp:
        Mode = "seeds"
        seedsList = []
        soilList = []
        fertilizerList = []
        waterList = []
        lightList = []
        temperatureList = []
        humidityList = []
        locationList = []
        for line in fp:
            workingLine = line.replace("\n", "")
            NewMode = getCurrentMap(workingLine.replace("\n", ""), Mode)
            if workingLine and NewMode == Mode:
                if "seeds" in Mode:
                    seedsList = createSeedList(workingLine)
                elif "soil" in Mode:
                    createMap(soilList, workingLine)
                elif "fertilizer" in Mode:
                    createMap(fertilizerList, workingLine)
                elif "water" in Mode:
                    createMap(waterList, workingLine)
                elif "light" in Mode:
                    createMap(lightList, workingLine)
                elif "temperature" in Mode:
                    createMap(temperatureList, workingLine)
                elif "humidity" in Mode:
                    createMap(humidityList, workingLine)
                elif "location" in Mode:
                    createMap(locationList, workingLine)
            Mode = NewMode
        outputList = checkMap(seedsList, soilList)
        outputList = checkMap(outputList, fertilizerList)
        outputList = checkMap(outputList, waterList)
        outputList = checkMap(outputList, lightList)
        outputList = checkMap(outputList, temperatureList)
        outputList = checkMap(outputList, humidityList)
        outputList = checkMap(outputList, locationList)
        print(min(outputList))


def pt1(filePath):
    with open(filePath, "r") as fp:
        Mode = "seeds"
        seedsList = []
        soilList = []
        fertilizerList = []
        waterList = []
        lightList = []
        temperatureList = []
        humidityList = []
        locationList = []
        for line in fp:
            workingLine = line.replace("\n", "")
            NewMode = getCurrentMap(workingLine.replace("\n", ""), Mode)
            if workingLine and NewMode == Mode:
                if "seeds" in Mode:
                    seedsList = workingLine.replace("seeds:", "").strip().split(" ")
                    seedsList = [int(i) for i in seedsList]

                elif "soil" in Mode:
                    createMap(soilList, workingLine)
                elif "fertilizer" in Mode:
                    createMap(fertilizerList, workingLine)
                elif "water" in Mode:
                    createMap(waterList, workingLine)
                elif "light" in Mode:
                    createMap(lightList, workingLine)
                elif "temperature" in Mode:
                    createMap(temperatureList, workingLine)
                elif "humidity" in Mode:
                    createMap(humidityList, workingLine)
                elif "location" in Mode:
                    createMap(locationList, workingLine)
            Mode = NewMode
        outputList = checkMap(seedsList, soilList)
        outputList = checkMap(outputList, fertilizerList)
        outputList = checkMap(outputList, waterList)
        outputList = checkMap(outputList, lightList)
        outputList = checkMap(outputList, temperatureList)
        outputList = checkMap(outputList, humidityList)
        outputList = checkMap(outputList, locationList)
        print(min(outputList))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="AOC Day5")
    parser.add_argument("-f", "--file", required="True")
    args = parser.parse_args()
    pt1(args.file)
    pt2(args.file)
