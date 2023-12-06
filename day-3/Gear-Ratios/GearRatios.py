
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
        readyToValidate = (not char.isnumeric() or index==len(currLine)-1)
        if char.isnumeric(): #If current char is digit add and continue
            canidate = canidate + char 
        if canidate and readyToValidate: #If we have a canidate but our current char check if validity of canidate
            startPoint = index-len(canidate)-1 if index-len(canidate)-1 > 0 else 0
            stopPoint = index+1
            if (
                    listContainsSymbol(prevLine[startPoint:stopPoint]) or #Check row above extended in either directio +1
                    listContainsSymbol(currLine[startPoint:stopPoint]) or   #Check the current char & the char before canidate
                    
                    listContainsSymbol(nextLine[startPoint:stopPoint])    #Check row below extended in either directio +1 
                    ):
                result += int(canidate)
            canidate = ""
    return result

def openData(fPath: str) -> int:
    total = 0
    totalGear = 0
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
                #totalGear += findGear(currLine, nextLine, prevLine)
                prevLine = currLine
                currLine = nextLine
    #totalGear += findGear(currLine, nextLine, prevLine)
    total += processLine(currLine, [], prevLine) #Process last line
    print(f'Total: {total}, total Gear {totalGear}')
    return total 


def findGear(currLine: list, nextLine: list = [], prevLine: list = []) -> int:
    result = 0
    for index, char in enumerate(currLine):
        if char == "*":
            print(f"Potential Gear found at {index-1}")
            startPoint = index-4 if index-4 >= 0 else 0
            endPoint = index+3
            canidates = []
            for line in [currLine, nextLine, prevLine]:
                canidate = gearValue(line, index-1)
                print(canidate)
                #`canidates.append(*canidate) if len(canidate) > 0 else None
            if len(canidates) == 2:
                result += (canidates[0] * canidates[1])
    return result

def gearValue(line: list, index: int) -> int:
    result = []
    canidate = ""
    for idx, char in enumerate(line):
        readyToValidate = (not char.isnumeric() or idx == len(line)) # check if we've reached the end of the digit or line
        if char.isnumeric():
            canidate += char
        if canidate and readyToValidate:
            if index >= idx-len(canidate) and index <= idx+1:
                result.append(int(canidate))
            else:
                canidate = ""
    return result
        





