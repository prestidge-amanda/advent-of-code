from os.path import abspath
import re

fPath = abspath("2020\day_1\input.txt")
file1=open(fPath,"r")
numbers=file1.readlines()

for number1 in numbers:
    for number2 in numbers:
        if (int(number1)+int(number2)==2020):
            print(int(number1)*int(number2))
            break;