def block1(a,b,c):
    if (a*-1 + b + c) > 1.5:
        return 1
    return 0
def block2(a,b,c):
    if (a - b - c) > 0.5:
        return 1
    return 0
    
def testNeuron(a,b,c):
    y1 = block1(a,b,c)
    y2 = block2(a,b,c)
    #print y1, y2
    if (y1+y2) > 0:
        print a,b,c,"1"
    else:
        print a,b,c,"0"

for x in range(0,2,1):
    for y in range(0,2,1):
        for z in range(0,2,1):
            testNeuron(x,y,z)
