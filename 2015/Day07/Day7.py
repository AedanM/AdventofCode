import argparse
import ctypes
from pprint import pp


def LookupFunc(string):
    circuit = string.split(" ")
    result = (None, None, None)
    match circuit[1]:
        case "AND":
            result = (circuit[4], lambda x, y: x & y, (circuit[0], circuit[2]))
        case "OR":
            result = (circuit[4], lambda x, y: x | y, (circuit[0], circuit[2]))
        case "LSHIFT":
            result = (circuit[4], lambda x, y: x << y, (circuit[0], circuit[2]))
        case "RSHIFT":
            result = (circuit[4], lambda x, y: x >> y, (circuit[0], circuit[2]))
        case _others:
            if circuit[0] == "NOT":
                result = (circuit[3], lambda x, y: ctypes.c_uint16(~x).value, (circuit[1], "0"))
            else:
                result = (circuit[2], lambda x, y: x, (circuit[0], "0"))
    return result


def SortCircuits(circuit):
    result = sum([ord(x) for x in circuit[0]])
    if str(circuit[2][0]).isnumeric():
        result -= 1000
    if str(circuit[2][1]).isnumeric():
        result -= 1000
    return result


def main(filePath):
    results = {}
    circuits = []
    with open(filePath, "r") as fp:
        for line in fp.readlines():
            circuits.append(LookupFunc(line.replace("\n", "")))
    circuits = sorted(circuits, key=lambda x: SortCircuits(x))
    skipped = []
    for dst, func, args in circuits:
        try:
            x = results[args[0]] if not args[0].isnumeric() else int(args[0])
            y = results[args[1]] if not args[1].isnumeric() else int(args[1])
            results[dst] = func(x, y)
        except KeyError:
            skipped.append((dst, func, args))
    print(len(circuits), len(skipped))
    for dst, func, args in skipped:
        x = results[args[0]] if not args[0].isnumeric() else int(args[0])
        y = results[args[1]] if not args[1].isnumeric() else int(args[1])
        results[dst] = func(x, y)
    pp(results)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="AOC Day7")
    parser.add_argument("-f", "--file", required=True)
    args = parser.parse_args()
    main(args.file)
