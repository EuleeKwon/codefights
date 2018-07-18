def addBorder(picture):
    output = []
    border = ""
    for i in range(len(picture[0])+2):
        border += "*"
    output.append(border)
    for i in range(len(picture)):
        output.append("*"+picture[i]+"*")  
    output.append(border)
    
    return output