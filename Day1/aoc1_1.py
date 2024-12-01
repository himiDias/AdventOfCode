inp = open("input1.txt")

array1 = []
array2 = []

for line in inp:
    x = line.split("   ")
    array1.append(x[0])
    array2.append(x[1])



 
      
array1.sort()
array2.sort()

distance = 0
for i in range(0,len(array1)):
    diff = int(array1[i]) - int(array2[i])
    if (diff<0):
        distance = distance + (diff *-1)
    else:
        distance = distance + diff
    
print(distance)

 
 