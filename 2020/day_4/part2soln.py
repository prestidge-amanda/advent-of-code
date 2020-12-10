from os.path import abspath
import re

fPath = abspath("C:\\Users\\owner\\Desktop\\advent_of_code\\day_4\\input.txt")
file1=open(fPath,"r")
passportList=file1.readlines()
expectedFields=["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"]
passports=[]
passportsData=[]
currPassport=[]
currData=[]

for line in passportList:
    if(len(line)!=1):
        entries=line.split(":")
        for element in entries:
            if(element.find(' ')>-1):
                currPassport.append(element.split(' ')[1])
                currData.append(element.split(' ')[0])
            elif(element.find('\n')==-1):    
                currPassport.append(element)
            else:
                currData.append(element[:-1])
    else:
        passports.append(currPassport)
        passportsData.append(currData)
        currPassport=[]
        currData=[]

passportsData.append(currPassport)
passportsData.append(currData)
validPassports=0

for passport, passportData in zip(passports, passportsData):
    currGood=True
    for field in expectedFields:
        if(field not in passport):
            if(field!='cid'):
                currGood=False
            break
        pos=passport.index(field)
        if(field=='byr' and (not passportData[pos].isdecimal() or len(passportData[pos])!=4 or int(passportData[pos])>2002 or int(passportData[pos])<1920)):
            currGood=False
            break
        elif(field=='iyr' and (not passportData[pos].isdecimal() or len(passportData[pos])!=4 or int(passportData[pos])<2010 or int(passportData[pos])>2020)):
            currGood=False
            break
        elif(field=='eyr' and (not passportData[pos].isdecimal() or len(passportData[pos])!=4 or int(passportData[pos])<2020 or int(passportData[pos])>2030)):
            currGood=False
            break
        elif(field=='pid' and (len(passportData[pos])!=9 or not passportData[pos].isdecimal())):
            currGood=False
            break
        elif(field=='hgt' and not re.match("^[0-9]+(in|cm)$", passportData[pos])):
            currGood=False
            break
        elif(field=='hcl' and not re.match("^#[0-9a-f]{6}$", passportData[pos])):
            currGood=False
            break
        elif(field=='ecl' and not re.match("^(amb|blu|brn|gry|grn|hzl|oth)$",passportData[pos])):
            currGood=False
            break
    if(currGood==True):
        validPassports+=1

print(validPassports)