
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
    totalGear = []
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
                old = totalGear
                total += processLine(currLine, nextLine, prevLine)
                result = findGear(currLine, nextLine, prevLine)
                totalGear.append(result)
                print(f'Curr line: {lineIndex-1} with result {result}')
                print('--------------------')
                prevLine = currLine
                currLine = nextLine
    totalGear.append(findGear(currLine, nextLine, prevLine))
    #print(f'Final line: {lineIndex}, with old total: and final total {totalGear}')
    total += processLine(currLine, [], prevLine) #Process last line
    print(f'Total: {total}, total Gear {sum(totalGear)}')
    return (total, sum(totalGear)) 


def findGear(currLine: list, nextLine: list = [], prevLine: list = []) -> int:
    result = 0
    for index, char in enumerate(currLine):
        if char == "*":
            startPoint = index-3 if index-3 >= 0 else 0
            endPoint = index+4
            canidates = []
            adjIndex = 3 #currLine[startPoint:endPoint].index('*')
            for line in [currLine[startPoint:endPoint], nextLine[startPoint:endPoint], prevLine[startPoint:endPoint]]:
                print(f'Current line {line}, start point: {startPoint}, end point: {endPoint}')
                canidates.extend(gearValue(line, adjIndex))
            if len(canidates) == 2:
                print(f"{canidates[0]},{canidates[1]}")
                result += (canidates[0] * canidates[1])
    return result

def gearValue(line: list, index: int) -> int:
    result = []
    canidate = "" 
    canidateRange = []
    for idx, char in enumerate(line):
        readyToValidate = (not char.isnumeric() or idx == len(line)-1) # check if we've reached the end of the digit or line
        if char.isnumeric():
            canidate += char
            canidateRange.append(idx)
        if canidate and readyToValidate:
            print(f'Currently validating canidate: {canidate} if {index} is {[*canidateRange, canidateRange[0]-1, canidateRange[len(canidateRange)-1]+1]}')
            if index in [*canidateRange, canidateRange[0]-1, canidateRange[len(canidateRange)-1]+1]:
                #print(f'canidate {canidate} is valid')
                result.append(int(canidate))
            canidate = ""
            canidateRange = []
    return result
        





