


def listContainsSymbol(input: list) -> bool:
    invalidChars = {'.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    for char in input:
        if char in invalidChars:
            pass
        else:
            return True
    return False
