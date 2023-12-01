import os

def recArrSum(arr: array('I'), len: int) -> int:
    '''
    desc: Meant to recursively sum an array of ints
    input: array of unsigned integers
    output: unsigned integer representing the sum of the array
    '''
    if len > 2:
        halfLen = len/2
        leftSum  = recArrSum(arr[:halfLen], halfLen)
        rightSum = recArrSum(arr[halfLen:], halfLen)
        return lefSum + rightSum
    else:
        return arr[0] + arr[1]

def lineProcessor(line: str) -> int:
    '''
    desc: takes in a string of mixed chars and digits, and returns the first and last digits cobimned into a two digit int ex. 6 & 5 would be 65
    input: string
    output: int
    '''
    digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
    los = len(line) # LOS = length of string
    firstDig = 'x'
    lastDig  = 'x'
    for char in str:
        if char in d
            firstDig = char
    for i in range(0, los):
        if str[los-i] in digits:
            lastDig = str[los-i]
    return int(firstDig + lastDig)

def loadInput(path: str) -> int:
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
        print(f"Begining to read in file: {path}"
        with os.open(path, 'r') as f:
            digToSum.append(lineProcessor(f.read()))
            lenOfFile += 1
    except Exception as e:
        print(f'Error opening {path} do to {e}')
    os.close(path)
    if digToSum:
        print(f"Starting to sum all {lenOfFile} from {path}")
        return recArrSum(digToSum)
    else:
        print('Error no data sum...')

