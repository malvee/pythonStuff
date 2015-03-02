def twoDimensionalArray(row, column):
    array = []
    for x in range(0,row,1):
        subArray = []
        for y in range(0,column,1):
            subArray.append(y+1)
        array.append(subArray)
    return array
array = twoDimensionalArray(2,3)
print array
