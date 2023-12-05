
def listContainsSymbol(input: list) -> bool:
    print(f'checking if line has symbols... {input}')
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
        print(f'Handling char {char}, at index {index}, {len(currLine)-1} if statement {readyToValidate}')
        if char.isnumeric(): #If current char is digit add and continue
            canidate = canidate + char 
        if canidate and readyToValidate: #If we have a canidate but our current char check if validity of canidate
            print(f'Checking validity for canidate {canidate}')
            startPoint = index-len(canidate)-1 if index-len(canidate)-1 > 0 else 0
            stopPoint = index+1
            if (
                    listContainsSymbol(prevLine[startPoint:stopPoint]) or #Check row above extended in either directio +1
                    listContainsSymbol(currLine[startPoint:stopPoint]) or   #Check the current char & the char before canidate
                    
                    listContainsSymbol(nextLine[startPoint:stopPoint])    #Check row below extended in either directio +1 
                    ):
                print(f'Canidate: {canidate} is valid adding to total {result} = {result + int(canidate)}')
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
                print('---------------------------------------------------')
                print(f'Finished currLine {lineIndex} for a total value: {total}')
                print('---------------------------------------------------')

    total += processLine(currLine, [], prevLine) #Process last line
    print(f'Total: {total}')
    return total



                
                



