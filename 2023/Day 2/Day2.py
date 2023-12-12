import argparse


class singleGame:
    def __init__(self, green, red, blue):
        self.green = green
        self.red = red
        self.blue = blue

    def __str__(self):
        return f"{self.green}g {self.red}r {self.blue}b"

    def __repr__(self):
        return f"{self.green}g {self.red}r {self.blue}b"

    def power(self):
        return self.green * self.blue * self.red


class GameRun:
    def __init__(self, gameId, gameLogs):
        self.gameId = gameId
        self.games = self.parseLogs(gameLogs)
        self.setMaxVals()

    def parseLogs(self, gameString):
        splitGames = gameString.split(";")
        gameLog = []
        for game in splitGames:
            splitSingleGame = game.split(",")
            greenCount, redCount, blueCount = 0, 0, 0
            for color in splitSingleGame:
                if "green" in color:
                    greenCount = int(color.replace("green", "").strip())
                if "blue" in color:
                    blueCount = int(color.replace("blue", "").strip())
                if "red" in color:
                    redCount = int(color.replace("red", "").strip())
            thisGame = singleGame(greenCount, redCount, blueCount)
            gameLog.append(thisGame)
        return gameLog

    def setMaxVals(self):
        greenMax, redMax, blueMax = 0, 0, 0

        for game in self.games:
            if game.green > greenMax:
                greenMax = game.green
            if game.blue > blueMax:
                blueMax = game.blue
            if game.red > redMax:
                redMax = game.red

        self.maxVals = singleGame(greenMax, redMax, blueMax)

    def isPossible(self, maxGame):
        result = (
            (self.maxVals.green <= maxGame.green)
            and (self.maxVals.red <= maxGame.red)
            and (self.maxVals.blue <= maxGame.blue)
        )
        return result

    def __str__(self):
        return self.gameId + " " + str(self.games)


def main(filePath):
    gameList = []
    powerList = []
    maxSingleGame = singleGame(green=13, red=12, blue=14)
    with open(filePath, "r") as fp:
        for line in fp:
            gameID = int(line.split(":")[0].replace("Game", "").strip())
            thisGameRun = GameRun(gameID, (line.split(":")[1]))
            if thisGameRun.isPossible(maxSingleGame):
                gameList.append(thisGameRun.gameId)
            powerList.append(thisGameRun.maxVals.power())
        print(sum(gameList))  # part 1 result
        print(sum(powerList))  # part 2 result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="AOC Day2")
    parser.add_argument("-f", "--file", required="True")
    args = parser.parse_args()
    main(args.file)
