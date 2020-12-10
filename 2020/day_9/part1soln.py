from os.path import abspath
import re

fPath = abspath("2020\day_9\input.txt")
file1=open(fPath,"r")
xmasData=file1.readlines()
prev25=[]

for x in range(25):
    prev25.append(int(xmasData[x][:-1]))

for number in xmasData[25:]:
    foundPair=False
    for x in range(25):
        diff=int(number[:-1])-int(prev25[x])
        if(diff in (prev25[:x]+prev25[x+1:])):
            foundPair=True
    if(foundPair==False):
        print(number)
        break
    else:
        prev25.pop(0)
        prev25.append(int(number[:-1]))
