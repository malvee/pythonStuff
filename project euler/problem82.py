def twoDimensionalArray(row, column):
    array = []
    for x in range(0,row,1):
        subArray = []
        for y in range(0,column,1):
            subArray.append(0)
        array.append(subArray)
    return array
def solveColumn(a):
    array[79][a] = array2[79][a]+array[79][a+1]
    for x in range(78, -1, -1):
        if array[x+1][a] < array[x][a+1]:
            array[x][a] = array2[x][a]+array[x+1][a]
        else:
            array[x][a] = array2[x][a]+array[x][a+1]
    for x in range(1, 80, 1):
        if array[x][a] - array2[x][a]>array[x-1][a]:
            array[x][a] = array[x-1][a]  + array2[x][a]
            
    
array = twoDimensionalArray(80,80)
array2 = twoDimensionalArray(80,80)
f = open("matrix82.txt", "r")
row = 0
column = 0
for x in f:
    line = x.split(",")
    for z in line:
        array[row][column] = int(z)
        column += 1
    column = 0
    row += 1
for x in range(80):
    for y in range(80):
        array2[x][y] = array[x][y]

for x in range(78,  -1, -1):
    solveColumn(x)
mini = 9999999
for x in range(80):
    if array[x][0] < mini:
        mini = array[x][0]
print mini
