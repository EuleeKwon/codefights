def allLongestStrings(inputArray):
    longest = max([len(inputArray[i]) for i in range(len(inputArray))])
    newlist = list()
    for i in range(len(inputArray)):
        if len(inputArray[i]) == longest:
             newlist.append(inputArray[i])
    return newlist
