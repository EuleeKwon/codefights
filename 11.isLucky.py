def isLucky(n):
    n = str(n)
    half = int(len(n)/2)
    sum1 = 0
    sum2 = 0
    for i in range(half):
        sum1+=int(n[i])
        sum2+=int(n[len(n)-i-1])
    if sum1 == sum2:
        return True
    else:
        return False