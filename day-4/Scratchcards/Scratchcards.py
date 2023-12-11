


def readCardStack(path: str) -> int:
    index = 1
    result = 0
    multiple = 1
    results = {}
    with open(path, 'r') as f:
        for line in f:
            myNumbers, winningNumbers = line.replace('\n', '').split('|')
            winningNumbers = winningNumbers.split(' ')
            myNumbers = myNumbers.replace(f'Card {index}: ', '').split(' ')
            winningNumbers = set([num for num in winningNumbers if num])
            myNumbers = [num for num in myNumbers if num]
            matches = findWinners(myNumbers, winningNumbers)
            results[index] = {'matches': matches, 'numOfCopies':  1}
            index += 1
    totalCards = 0
    for id, value in results.items():
        depth = value['matches']
        totalCards+= value['numOfCopies']
        if depth != 0:
            for i in range(id+1, id+depth+1):
                results[i]['numOfCopies'] += value['numOfCopies']
    return totalCards
    
def findWinners(myNumbers: list[int], winningNumbers: set[int]) -> int:
    point = 0
    for number in myNumbers:
        if number in winningNumbers:
            point += 1
    return point

