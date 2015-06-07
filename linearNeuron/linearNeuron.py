w1 = 0
w2 = 0
w3 = 0
learningRate = 0.00001
f = open('nndata', 'r')
for i in range(1000):
	x = f.readline()
	stringArray  = x.split(" ")
	a = float(stringArray[0])
	b = float(stringArray[1])
	c = float(stringArray[2])
	d = float(stringArray[3]) 
	resError = d - (w1 * a + w2 * b + w3 * c)  
	#print resError
	w1 +=  learningRate * resError * a
	w2 +=  learningRate * resError * b
	w3 += learningRate * resError * c
print w1, w2, w3