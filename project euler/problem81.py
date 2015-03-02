def twoDimensionalArray(row, column):
    array = []
    for x in range(0,row,1):
        subArray = []
        for y in range(0,column,1):
            subArray.append(y+1)
        array.append(subArray)
    return array
def minimumx(a, b):
    if a < b:
        return a
    return b
array = twoDimensionalArray(80,80)
f = open("matrix.txt", "r")
row = 0
column = 0
for x in f:
    line = x.split(",")
    for z in line:
        #print row, column
        array[row][column] = int(z)
        column += 1
    column = 0
    row += 1


for x in range(78,-1,-1):
    array[79][x] += array[79][x+1]
for y in range(78,-1,-1):
    array[y][79] += array[y+1][79]
for x in range(78, -1, -1):
    for y in range(78,-1,-1):
        array[x][y] += minimumx(array[x][y+1], array[x+1][y])
print array[0][0]
    
f.close()
