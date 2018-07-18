def arrayMaximalAdjacentDifference(inputArray):
    maximum = 0
    new_max = 0
    for i in range(len(inputArray)-1):
        maximum = abs(inputArray[i+1] - inputArray[i])
        if new_max <= maximum:
            new_max = maximum
    return new_max