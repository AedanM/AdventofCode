import argparse


class landmark:
    def __init__(self, startingX, startingY, endingX, endingY, value):
        self.startingX = startingX
        self.startingY = startingY
        self.endingX = endingX
        self.endingY = endingY
        self.value = value
        self.startCoord = (startingX, startingY)
        self.endCoord = (endingX, endingY)
        self.used = False

    def __str__(self):
        return f"{self.value} {self.startCoord} {self.endCoord}"

    def __repr__(self):
        return f"{self.value} {self.startCoord} {self.endCoord}"


def withinOne(num, target):
    return (num == target) or (num + 1 == target) or (num - 1 == target)


def main(filePath):
    numArray = []
    gearArray = []
    usedList = []
    with open(filePath, "r") as fp:
        for Yidx, line in enumerate(fp):
            currentNum = ""
            startXidx = 0
            startYidx = 0
            for Xidx, char in enumerate(line):
                if not (char == "." or char == "\n"):
                    if char.isnumeric():
                        if currentNum == (""):
                            startXidx = Xidx
                            startYidx = Yidx
                        currentNum += char
                    else:
                        newGear = landmark(Xidx, Yidx, Xidx, Yidx, char)
                        gearArray.append(newGear)
                else:
                    if currentNum:
                        endingX = Xidx
                        endingY = Yidx
                        if startXidx == Xidx:
                            endingY -= 1
                        elif startYidx == Yidx:
                            endingX -= 1
                        newNum = landmark(startXidx, startYidx, Xidx, Yidx, currentNum)
                        numArray.append(newNum)
                        currentNum = ""
                        startXidx = ""
                        startYidx = ""
    runningSum = 0
    for gear in gearArray:
        print(f"\n\n-----------Using {gear}----------------")
        for num in numArray:
            Xtouching = withinOne(num.startingX, gear.startingX) or withinOne(
                num.endingX, gear.startingX
            )
            Ytouching = withinOne(num.startingY, gear.startingY) or withinOne(
                num.endingY, gear.startingY
            )
            if Xtouching and Ytouching and not num.used and (int(num.value) not in usedList):
                num.used = True
                print(f"Number {num.value} ({num.startCoord})used here")
                usedList.append(int(num.value))
                runningSum += int(num.value)
    print(runningSum)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="AOC Day2")
    parser.add_argument("-f", "--file", required=True)
    args = parser.parse_args()
    main(args.file)
