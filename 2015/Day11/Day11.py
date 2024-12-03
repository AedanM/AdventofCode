""" Oopsie did this with pen & paper lol"""

import re
import sys
from pathlib import Path


def IncString(string):
    return (
        string[:-1] + chr(ord(string[-1]) + 1)
        if string[-1] != "z"
        else IncString(string[:-1]) + "a"
    )


def CheckStraight(s):
    sCount = -1
    lVal = -1
    for c in s:
        if ord(c) == lVal + 1:
            sCount += 1
            if sCount > 2:
                return True
        else:
            sCount = 0
        lVal = ord(c)
    return False


def CheckPairs(s):
    count = 0
    for x in set(s):
        count += len(re.findall(f"{x}{{2}}", s))
    return count > 1


def Main(s: str):
    passP = False
    while not passP:
        passP = not any(x in ["i", "o", "l"] for x in s)

        passP = passP and CheckStraight(s)
        passP = passP and CheckPairs(s)
        # passP = (
        #     passP
        #     and len([x for idx, x in enumerate(s) if idx != len(s) - 1 and x != s[idx + 1]]) > 1
        # )
        if not passP:
            s = IncString(s)
    return s


if __name__ == "__main__":
    inStr = "hepxcrrq"
    print(Main(inStr))
