def makeArrayConsecutive2(statues):
    start = min(statues)
    last = max(statues)
    string = range(start+1,last)
    count = 0
    for i in range(len(string)):
        if string[i] in statues:
            i =+1
        else:
            count +=1
            i =+1
    return(count)
            
            
        
