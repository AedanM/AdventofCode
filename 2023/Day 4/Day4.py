import argparse


class Card:
    def __init__(self, CardLine, cardsWon):
        self.num = CardLine.split(":")[0][-1]
        self.winningNums = [
            int(x) for x in CardLine.split("|")[0].split(":")[1].split(" ") if x
        ]
        self.userNums = [int(x) for x in CardLine.split("|")[1].split(" ") if x]
        self.winMul = 0
        self.matches = 0
        self.cardsWon = cardsWon

    def calcMatchesAndPoints(self):
        winMul = 0
        matches = 0
        for num in self.winningNums:
            if num in self.userNums:
                matches += 1
                if winMul == 0:
                    winMul = 1
                else:
                    winMul *= 2
        self.winMul = winMul
        self.matches = matches
        return winMul

    def __repr__(self):
        return self.num


def main(filePath):
    with open(filePath, "r") as fp:
        score = 0
        fileTxt = [x for x in fp]
        cardArray = [1] * len(fileTxt)
        totalCards = 0
        for idx, line in enumerate(fileTxt):
            newCard = Card(line, cardArray[idx])
            winMul = newCard.calcMatchesAndPoints()
            cardArray.append(newCard)
            score += winMul
            if newCard.matches:
                for i in range(1, newCard.matches + 1):
                    cardArray[idx + i] += 1 * newCard.cardsWon
            totalCards += newCard.cardsWon

    print(f"Part 1: {score}")
    print(f"Part 2: {totalCards}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="AOC Day4")
    parser.add_argument("-f", "--file", required="True")
    args = parser.parse_args()
    main(args.file)
