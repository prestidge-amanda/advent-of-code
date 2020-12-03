from os.path import abspath
import re

fPath = abspath("2020\day_2\input.txt")
file1=open(fPath,"r")
numValidPasswords=0
passwordInfos=file1.readlines()

for passwordInfo in passwordInfos:
    minLetterOccur=int(passwordInfo.split('-')[0])
    maxLetterOccur=int(passwordInfo.split('-')[1].split()[0])
    letter=passwordInfo.split()[1][0]
    password=passwordInfo.split(":")[1]
    occurence=password.count(letter)
    if(occurence>=minLetterOccur and occurence<=maxLetterOccur): 
        numValidPasswords+=1

print(numValidPasswords)
file1.close();