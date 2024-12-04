import time

import re

startt = time.time()

def findmul(line):
    reg = re.findall("mul\([\\d]+,[\\d]+\)",line)
    all.append(reg)

inp = open("Day3/input3.txt")
all = []

do = True
linemain = ""
for line in inp:
    linemain = linemain+line
     

while True:
    if(do):
        reg1 = re.search("don't\(\)",linemain)
        if(reg1):
            start = reg1.start()
            end = reg1.end()
            do = False
        else:
            start = len(line)
            part = linemain[:start]
            findmul(part)
            break

        #print(start)
        part = linemain[:start]
        linemain = linemain[end:]
        findmul(part)

    if(not do):
        reg2 = re.search("do\(\)",linemain)
        if (reg2):
            end1 = reg2.end()
            linemain = linemain[end1:]
            do = True
        else:
            break


 

result = 0

for i in all:
    for j in i:
        reg1 = re.findall("[\\d]+",j)
        #print(reg1)
        result = result + int(reg1[0]) * int(reg1[1])


 

print(time.time() - startt)
print(result)
 

# 0.002569437026977539 s