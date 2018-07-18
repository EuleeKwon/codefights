def areSimilar(a, b): 
    count = 0
    lista = []
    listb = []
    for i in range(len(a)):
        if a[i] != b[i]:
            count+=1
            lista.append(a[i])
            listb.append(b[i])
    if count == 0:
        return True
    elif count == 2:
        if set(lista) == set(listb):
            return True
        else:
            return False
    else:
        return False