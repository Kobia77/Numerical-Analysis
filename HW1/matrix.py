# work by: 
# Kobi Alen -318550985
# Matan Kahlon - 316550458
# Lior Engel - 315006783

matrix = [[1,-1,-2],[2,-3,-5],[-1,3,5]]

def print_matrix(matrix):
    max_len = max(len(str(element)) for row in matrix for element in row)
    format_str = f"{{:>{max_len}}}"
    for row in matrix:
        print(" ".join(format_str.format(element) for element in row))

def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Number of columns in the first matrix must equal number of rows in the second matrix.")
    rows_matrix1 = len(matrix1)
    cols_matrix1 = len(matrix1[0])
    cols_matrix2 = len(matrix2[0])
    result = [[0 for _ in range(cols_matrix2)] for _ in range(rows_matrix1)]
    for i in range(rows_matrix1):
        for j in range(cols_matrix2):
            for k in range(cols_matrix1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

def findInverseMat(mat):

    E=mat
    inverse=[[1,0,0],[0,1,0],[0,0,1]]
    I = [[1,0,0],[0,1,0],[0,0,1]]
    
    for j in range(3):
        for i in range(3):
            if i!=j and E[i][j]!=0:
                I[i][j]=-(E[i][j])/E[j][j]
                E = multiply_matrices(I,E)
                inverse = multiply_matrices(I,inverse)
                I = [[1,0,0],[0,1,0],[0,0,1]]
    for i in range(3):
        I[i][i]=1/E[i][i]
        E=multiply_matrices(I,E)
        inverse=multiply_matrices(I,inverse)
        I = [[1,0,0],[0,1,0],[0,0,1]]
    return inverse


def findNorm(mat):
    norm=0
    rowSum=0
    for i in range(3):
        for j in range(3):
            rowSum+=abs(mat[i][j])
        if rowSum>norm:
            norm=rowSum
        rowSum=0
    return norm


print("Matrix:")
print_matrix(matrix)
print("\n")
print("Inverse:")
print_matrix(findInverseMat(matrix))
print("\n")
inverse=findInverseMat(matrix)
print("found inverse\n")
matNorm=findNorm(matrix)
print("found matrix norm: ",matNorm,"\n")
inverseNorm=findNorm(inverse)
print("found inverse norm: ",inverseNorm,"\n")
COND=matNorm*inverseNorm
print("COND is: ",COND)
