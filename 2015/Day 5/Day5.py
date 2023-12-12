import argparse

Num_Vowels = 3


def checkDoubleLetter(inString):
    checkBool = False
    for idx, i in enumerate(inString):
        try:
            if i == inString[idx + 1]:
                checkBool = True
        except:
            pass
    return checkBool


def checkBadStrings(inString):
    checkBool = True
    bad_strings = ["ab", "cd", "pq", "xy"]
    for bad_string in bad_strings:
        if bad_string in inString:
            checkBool = False
    return checkBool


def checkVowels(inString):
    vowelCount = 0
    vowels = ["a", "e", "i", "o", "u"]
    for vowel in vowels:
        vowelCount += inString.count(vowel)
    return vowelCount >= Num_Vowels


def checkDoubleLetterWithSpace(inString):
    checkBool = False
    for idx, i in enumerate(inString):
        try:
            if i == inString[idx + 2]:
                checkBool = True
        except IndexError:
            pass
    return checkBool


def checkReappearingStrings(inString):
    checkBool = False
    for idx, i in enumerate(inString):
        try:
            substring = i + inString[idx + 1]
            if inString.count(substring) > 1:
                checkBool = True
        except IndexError:
            pass
    return checkBool


def main(filePath):
    NiceTotalPt1 = 0
    NiceTotalPt2 = 0
    with open(filePath, "r") as fp:
        for line in fp:
            line = line.replace("\n", "")
            if checkDoubleLetter(line) and checkBadStrings(line) and checkVowels(line):
                NiceTotalPt1 += 1
            if checkDoubleLetterWithSpace(line) and checkReappearingStrings(line):
                NiceTotalPt2 += 1
    print(NiceTotalPt1)
    print(NiceTotalPt2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="AOC Day5")
    parser.add_argument("-f", "--file", required="True")
    args = parser.parse_args()
    main(args.file)
