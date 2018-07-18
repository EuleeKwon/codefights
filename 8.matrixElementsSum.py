def matrixElementsSum(matrix):
    for row in range(len(matrix)-1):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                matrix[row+1][col] = 0
                
    return sum([sum(matrix[i]) for i in range(len(matrix))])
                
        
