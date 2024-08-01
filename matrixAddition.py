rows = int(input())
cols = int(input())

matrix1 = []
for i in range(rows):
    row1 = []
    for j in range(cols):
        element1 = int(input())
        row1.append(element1)
    matrix1.append(row1)


matrix2 = []
for i in range(rows):
    row2 = []
    for j in range(cols):
        element2 = int(input())
        row2.append(element2)
    matrix2.append(row2)

matrix3 = []
for i in range(rows):
    row3 = []
    for j in range(cols):
        row3.append(matrix1[i][j] + matrix2[i][j])
    matrix3.append(row3)


print(" Resultant Matrix:")
for row in matrix3:
    for element in row:
        print(element, end=' ')
    print()  
