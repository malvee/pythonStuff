# 150a + 50b + 100c = d
import random
import os

def main():
    os.chdir("C:\Users\pranav\Desktop\sparkeye")
    file = open("nndata", "w")
    for i in range(0,1000):
        a = random.randint(0,100)
        b = random.randint(0,100)
        c = random.randint(0,100)
        d = 150*a + 50*b + 100*c
        file.write("%d %d %d %d\n" % (a,b,c,d))
    file.close()
if __name__ == '__main__':
    main()
