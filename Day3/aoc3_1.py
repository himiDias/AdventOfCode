import re
import time

start = time.time()

inp = open("Day3/input3.txt")
all = []
for line in inp:
    reg = re.findall("mul\([\\d]+,[\\d]+\)",line)
    all.append(reg)

#print(all)

result = 0

for i in all:
    for j in i:
        reg1 = re.findall("[\\d]+",j)
        #print(reg1)
        result = result + int(reg1[0]) * int(reg1[1])


print(result)

print(time.time()-start)

#0.002864837646484375 s