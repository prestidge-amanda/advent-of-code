from os.path import abspath

fPath = abspath("C:\\Users\\owner\\Desktop\\advent_of_code\\day_4\\input.txt")
file1=open(fPath,"r")
passportList=file1.readlines()
expectedFields=["byr","iyr","eyr","hgt","hcl","ecl","pid"]
passports=[]
currPassport=[]

for line in passportList:
    if(len(line)!=1):
        entries=line.split(":")
        for element in entries:
            if(element.find(' ')>-1):
                currPassport.append(element.split(' ')[1])
            elif(element.find('\n')==-1):    
                currPassport.append(element)
    else:
        passports.append(currPassport)
        currPassport=[]

passports.append(currPassport)
validPassports=0

for passport in passports:
    currGood=True
    for field in expectedFields:
        if(field not in passport):
            currGood=False
    if(currGood==True):
        validPassports+=1

print(validPassports)
