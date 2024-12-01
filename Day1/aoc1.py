import time

start = time.time()
inp = open("input1.txt")

array1 = []
array2 = []

for line in inp:
    x = line.split("   ")
    array1.append(x[0])
    array2.append(x[1])


#print(array1[2])
 
def part1():        
    array1.sort()
    array2.sort()

    distance = 0
    for i in range(0,len(array1)):
        diff = int(array1[i]) - int(val2)
        if (diff<0):
            distance = distance + (diff *-1)
        else:
            distance = distance + diff
        
    print(distance)

def part2(array1,array2):
    
    array1.sort()
    array2.sort()

    print(array1,array2)
    pos = 0
    val = int(array1[pos])
    i = 0
    count = 0
    score = 0
     
    while i < len(array2):
        val2 = int(array2[i])
        print(val,val2)
        if val2 == val:
            while (i < len(array2) and val2 == val):
                count =count + 1
                i = i + 1
            if (i == len(array2)):
                score = score + (int(val) * count)
                break
            elif val2 > val:
                score = score + (int(val) * count)
                #print("score",score)
                pos = pos + 1
                while (pos < len(array1) and val == int(array1[pos])):
                    score = score + (int(val)*count)
                    pos = pos+ 1
                count = 0
                
                if (pos == len(array1)):
                    break

             
                val = int(array1[pos])
        elif val2 < val:
            i = i+1
        else:
            pos = pos +1
            if (pos == len(array1)):
                break
            val = int(array1[pos])
             
    
    print(score)


part2(array1,array2)

print("Exec : ", (time.time()- start))