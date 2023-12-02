
class CubeGame():
    def __init__(self, gameLine: str):
        '''
        input: Game 1: 10 green, 9 blue, 1 red; 1 red, 7 green
        desired output: {
            id:1,
            maxTypeObsv: {'green': 10, 'blue': 9, 'red': 1}
            rounds: [ {'green': 10, 'blue': 9, 'red': 1}, {'green': 7, 'blue': 0, 'red': 1}, ...]
        '''
        id, rawRounds = gameLine.split(":", 1)
        self.id = int(id.replace("Game ", ""))
        self.rounds = list()
        self.maxTypeObsv = dict()
        for round in rawRounds.split(";"):
            currRound = {}
            for color in round.split(","):
                colorName = color[3:].strip()
                colorValue = int(color[:3].strip())
                currRound[colorName] = colorValue
                if colorName in self.maxTypeObsv.keys():
                    # If we already have an entry for that color check if this one is larger, if it is replace the current one
                    self.maxTypeObsv[colorName] = colorValue if colorValue > self.maxTypeObsv[colorName] else self.maxTypeObsv[colorName] 
                else: # Else lets add the color entry to our max entries
                    self.maxTypeObsv[colorName] = colorValue
            self.rounds.append(currRound)
        
    def isPossible(self, maxColors: dict) -> bool:
        for key, value in maxColors.items():
            if key in self.maxTypeObsv.keys() and self.maxTypeObsv[key] > value:
                return False
        return True
        
def findPossibleGames(path: str, maxTypes: dict()) -> int:
    total = 0
    with open(path, 'r') as f:
        for gameLine in f:
            newGame = CubeGame(gameLine)
            if newGame.isPossible(maxTypes):
                total += newGame.id
    return total

def findMinSetPowered(path: str) -> int:
    total = 0
    with open(path, 'r') as f:
        for gameLine in f:
            newGame = CubeGame(gameLine)
            maxPower = 1
            for color, value in newGame.maxTypeObsv.items():
                maxPower *= value
            total += maxPower
    print(f"total {total}")
    return total
