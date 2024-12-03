import argparse

numDict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def getNums(lineStr):
    num1 = 0
    num1_idx = 0
    for idx, char in enumerate(lineStr):
        if char.isnumeric():
            if num1 == 0:
                num1_idx = idx
                num1 = int(char)
    num2 = 0
    num2_idx = 0
    for idx, char in enumerate(reversed(lineStr)):
        if char.isnumeric():
            if num2 == 0:
                num2_idx = idx
                num2 = int(char)

    # print(f'{lineStr} -> {num1*10 + num2}')
    return num1, num2


def findNames(lineStr):
    newStr = ""
    foundNums = []
    for key, value in numDict.items():
        if key in lineStr:
            idx = lineStr.index(key)
            ridx = lineStr.rindex(key)
            if idx != ridx:
                foundNums.append((ridx, numDict[key]))
            foundNums.append((idx, numDict[key]))
    for char in lineStr:
        if char.isnumeric():
            idx = lineStr.index(char)
            ridx = lineStr.rindex(char)
            if idx != ridx:
                foundNums.append((ridx, int(char)))
            foundNums.append((idx, int(char)))
    sortedNums = sorted(foundNums)
    for i, j in sortedNums:
        newStr += str(j)
    # print(f'{lineStr} -> {newStr}')
    return newStr


def main(filePath):
    numList = []
    numAndWordList = []
    with open(filePath, "r") as fp:
        for line in fp:
            line = line.replace("\n", "")
            replacedString = findNames(line)
            pt1TensDigit, pt1OnesDigit = getNums(line)
            tensDigit, onesDigit = getNums(replacedString)
            # print(f'{line} -> {tensDigit*10 + onesDigit}')

            numList.append((pt1TensDigit * 10) + pt1OnesDigit)
            numAndWordList.append((tensDigit * 10) + onesDigit)
            # print('----------')
        print(f"Part 1: {sum(numList)}")
        print(f"Part 2: {sum(numAndWordList)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="AOC Day1")
    parser.add_argument("-f", "--file", required=True)
    args = parser.parse_args()
    main(args.file)
