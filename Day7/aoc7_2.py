inp = open("Day7/input7.txt")

def increment(list):
        for i in range(0,len(list)):
             
            if list[i] == 2:
                    if len(list) == 1:
                        break
                    if list[i+1] < 2:
                        list[i] = 0
                        list[i+1] += 1
                        break
                    else:
                        if i < len(list)-2:
                            list[i] = 0
                            next
                        else:
                            break
            else:
                list[i] += 1
                break
             

 
 
                   
sum = 0
for line in inp:
    line = line.strip().split(":")
    line[0] = int(line[0])
    line[1] = list(map(int,line[1].split()))

    ans = line[0]
    vals = line[1]
    spaces = len(line[1]) - 1
    space_vals = [0]*spaces
    
    while True:
        #print(space_vals)
        a = vals[0]
        for i in range(1,len(vals)):
            if space_vals[i-1] == 0:
                a = a + vals[i]
            elif space_vals[i-1] == 1:
                if (a == 0):
                    a = 1
                a = a * vals[i]
            else:
                a = int(str(a) + str(vals[i]))
        
        #print(ans,a)
        if (a == ans):
            sum = sum + ans
            break
        
        if (space_vals == [2]*spaces):
            break
        else:
            increment(space_vals)
        

print(sum)
