from os.path import abspath
import re

fPath = abspath("2020\day_2\input.txt")
file1=open(fPath,"r")
numValidPasswords=0
passwordInfos=file1.readlines()

for passwordInfo in passwordInfos:
    posn1=int(passwordInfo.split('-')[0])-1
    posn2=int(passwordInfo.split('-')[1].split()[0])-1
    letter=passwordInfo.split()[1][0]
    password=passwordInfo.split()[2]
    if(password[posn1]==letter and password[posn2]!=letter):
        numValidPasswords=numValidPasswords+1
    elif(password[posn1]!=letter and password[posn2]==letter):
        numValidPasswords=numValidPasswords+1

print(numValidPasswords)
file1.close();