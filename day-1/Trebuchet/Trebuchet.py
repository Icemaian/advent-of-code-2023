from array import array
def recArrSum(arr: array('I')) -> int:
    '''
    desc: Meant to recursively sum an array of ints
    input: array of unsigned integers
    output: unsigned integer representing the sum of the array
    '''
    arrLen = len(arr)
    if arrLen == 1:
        return arr[0]
    elif arrLen > 2:
        halfLen = arrLen//2
        leftSum  = recArrSum(arr[:halfLen])
        rightSum = recArrSum(arr[halfLen:])
        return leftSum + rightSum
    else:
        result = 0
        for i in range(0,arrLen):
            result += arr[i]
        return result

def lineProcessor(line: str) -> int:
    '''
    desc: takes in a string of mixed chars and digits, and returns the first and last digits cobimned into a two digit int ex. 6 & 5 would be 65
    input: string
    output: int
    '''
    original = line
    digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
    postRep = line
    los = len(line) # LOS = length of string
    firstDig = 'x'
    lastDig  = 'x'
    for char in line:
        if char in digits:
            firstDig = char
            break
    for i in range(0, los):
        if line[los-i-1] in digits:
            lastDig = line[los-i-1]
            break
    return int(firstDig + lastDig)

def digitStrReplacement(line: str) -> int:
    digits = {
        'one'   : '1',
        'two'   : '2',
        'three' : '3', 
        'four'  : '4',
        'five'  : '5',
        'six'   : '6',
        'seven' : '7',
        'eight' : '8',
        'nine'  : '9',
    }
    firstDig = '0'
    lastDig = '0'
    # Starting at the front
    lineLen = len(line)
    window = ""
    for i in range(0, lineLen):
        window += line[i]
        for key, value in digits.items():
            if key in window:
                firstDig = value
                break
            elif value in window:
                firstDig = value
                break
        if firstDig != '0':
            break
        if len(window) > 5:
            window = window[1:6]

    # Now doing the back
    window = ""
    for i in range(1, lineLen+1):
        window = line[lineLen-i] + window
        for key, value in digits.items():
            if key in window:
                lastDig = value
                break
            elif value in window:
                lastDig = value
                break
        if lastDig != '0':
            break
        if len(window) > 4:
            window = window[:4]
    return int(firstDig + lastDig)

def loadInput(path: str, allowStrRep: bool = False) -> int:
    '''
    desc: Take a file of strings seperated by new lines to return the sum of the combination of the first and last digits of each line
    input: str representing a file path
    output: int
    '''
    if path == '':
        print('Path must be to file...')
        return 0
    digToSum = array('I')
    lenOfFile = 0
    try:
        print(f"Begining to read in file: {path}")
        with open(path, 'r') as f:
            for line in f:
                digToSum.append(digitStrReplacement(line) if allowStrRep else lineProcessor(line))
                lenOfFile += 1
    except Exception as e:
        print(f'Error opening {path} due to {e}')
        return
    if digToSum:
        print(f"Starting to sum all {lenOfFile} from {path}")
        result = recArrSum(digToSum)
        print(f'Result is = {result}')
        return result
    else:
        print('Error no data sum...')


