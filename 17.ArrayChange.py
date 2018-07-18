def arrayChange(inputArray):
    count = 0
    for i in range(len(inputArray)-1):
        while inputArray[i] >= inputArray[i+1]:
                c = inputArray[i+1]
                inputArray[i+1] = inputArray[i]+1
                count+= inputArray[i+1]-c
    return count
            