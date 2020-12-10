from os.path import abspath
import re


def treeEncounter(right,down,treemap,maxRight,maxDown):
    currDown=0
    currRight=0
    numTrees=0

    while(currDown<maxDown):
        if(treemap[currDown][currRight]=='#'):
            numTrees+=1
        currRight=(currRight+right)%maxRight
        currDown+=down
    
    return numTrees
    

slopes=[[1,1],[3,1],[5,1],[7,1],[1,2]]
fPath = abspath("2020\day_3\input.txt")
file1=open(fPath,"r")
treemap=file1.readlines()
maxDown=len(treemap)
maxRight=(len(treemap[0]))-1

result=1

for slope in slopes:
    result=result*treeEncounter(slope[0],slope[1],treemap,maxRight,maxDown)

print(result)





