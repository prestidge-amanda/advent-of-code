from os.path import abspath
import re

fPath = abspath("2020\day_9\input.txt")
file1=open(fPath,"r")
xmasData=file1.readlines()
MAGICNUM=133015568
MAGICNUMSTR="133015568\n"
run=[]

endRun=False
currentSum=0
run=[]

while(MAGICNUMSTR in xmasData):
    xmasData.remove(MAGICNUMSTR)

for x in range(len(xmasData)):
    for y in range(len(xmasData)-x):
        if(currentSum+int(xmasData[x+y][:-1])==MAGICNUM):
            currentSum+=int(xmasData[x+y][:-1])
            endRun=True
            run.append(int(xmasData[x+y][:-1]))
            break
        elif(currentSum+int(xmasData[x+y][:-1])<MAGICNUM):
            currentSum+=int(xmasData[x+y][:-1])
            run.append(int(xmasData[x+y][:-1]))
        else:
            currentSum=0
            run=[]
            break
    if(endRun!=False):
        break

print(min(run)+max(run))    
    

        

    
