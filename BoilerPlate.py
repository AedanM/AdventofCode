import argparse


def main(filePath):
    with open(filePath, "r") as fp:
        for line in fp:
            print(line)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="AOC DayXXX")
    parser.add_argument("-f", "--file", required=True)
    args = parser.parse_args()
    main(args.file)
