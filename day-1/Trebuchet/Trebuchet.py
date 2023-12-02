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
    digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
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
        print(f"Begining to read in file: {path}")
        with open(path, 'r') as f:
            for line in f:
                digToSum.append(lineProcessor(line))
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

