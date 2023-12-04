
def listContainsSymbol(input: list) -> bool:
    invalidChars = {'.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    for char in input:
        if char in invalidChars:
            pass
        else:
            return True
    return False

def processLine(currLine: list, nextLine: list = [], prevLine: list = []) -> int:
    result = 0
    canidate = ""
    for index, char in enumerate(currLine):
        if char.isnumeric(): #If current char is digit add and continue
            canidate = canidate + char 
        elif canidate and not char.isnumeric(): #If we have a canidate but our current char check if validity of canidate
            startPoint = index-len(canidate)-1 if index-len(canidate)-1 > 0 else 0
            stopPoint = index+1
            if (
                    listContainsSymbol(currLine[startPoint:stopPoint]) or   #Check the current char & the char before canidate
                    listContainsSymbol(nextLine[startPoint:stopPoint]) or #Check row below extended in either directio +1
                    listContainsSymbol(prevLine[startPoint:stopPoint])    #Check row below extended in either directio +1 
                    ):
                result += int(canidate)
            canidate = ""
    return result

def openData(fPath: str) -> int:
    total = 0
    currLine = []
    nextLine = []
    prevLine = []
    lineIndex = 0
    with open(fPath, 'r') as f:
        for line in f:
            line = list(line.replace("\n", ""))
            lineIndex += 1
            if len(currLine) == 0:
                currLine = list(line)
            else:
                nextLine = list(line)
                total += processLine(currLine, nextLine, prevLine)
                prevLine = currLine
                currLine = nextLine
    total += processLine(currLine, [], prevLine) #Process last line
    print(f'Total: {total}')
    return total



                
                



