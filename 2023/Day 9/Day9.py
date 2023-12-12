import argparse


def getPattern(a):
    workingArray = []
    for idx, i in enumerate(a):
        try:
            workingArray.append(a[idx + 1] - i)
        except:
            break
    return workingArray


def addLastElement(a):
    for idx, i in enumerate(a):
        if idx != 0:
            i.append(i[-1] + a[idx - 1][-1])
        else:
            i.append(0)
    return a[-1][-1]


def addFirstElement(a):
    for idx, i in enumerate(a):
        if idx != 0:
            i.insert(0, i[0] - a[idx - 1][0])
        else:
            i.insert(0, 0)
    return a[-1][0]


def main(filePath):
    with open(filePath, "r") as fp:
        runningSumPt1 = 0
        runningSumPt2 = 0
        for line in fp:
            outputArr = []
            lineArr = line.replace("\n", "").split(" ")
            lineArr = [int(i) for i in lineArr]
            outputArr.append(lineArr)
            while any(V != 0 for V in outputArr[-1]):
                outputArr.append(getPattern(outputArr[-1]))
            outputArr.reverse()
            newValPt1 = addLastElement(outputArr)
            newValPt2 = addFirstElement(outputArr)

            runningSumPt1 += newValPt1
            runningSumPt2 += newValPt2
            print(outputArr)
        print(runningSumPt1)
        print(runningSumPt2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="AOC Day9")
    parser.add_argument("-f", "--file", required="True")
    args = parser.parse_args()
    main(args.file)
