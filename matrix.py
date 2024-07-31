rows = int(input())
cols = int(input())

matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input())
        row.append(element)
    matrix.append(row)

print("Matrix:")
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()  
