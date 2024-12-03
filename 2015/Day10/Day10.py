import sys
from pathlib import Path


def Main(valStr):
    currentDigit = -1
    digitCount = 0
    outStr = ""
    for v in str(valStr):
        if int(v) != currentDigit:
            if currentDigit >= 0:
                outStr += f"{digitCount}{currentDigit}"
            currentDigit = int(v)
            digitCount = 0
        digitCount += 1
    outStr += f"{digitCount}{currentDigit}"
    return outStr


if __name__ == "__main__":
    v = "3113322113"
    for _i in range(0, 50):
        v = Main(v)
    print(len(v))
