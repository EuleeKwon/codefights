def palindromeRearranging(inputString):
    count = False
    for i in set(inputString):
        if inputString.count(i)%2 !=0:
            if count:
                return False
            else:
                count = True
    return True