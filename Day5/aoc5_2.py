inp = open("Day5/input5.txt")
 
rules = []
updates = []
flag = False
for line in inp:
    if line == "\n":
        flag = True
    
    if (flag):
        a = line.strip().split(",")
         
        updates.append(a)
    else:
        a = line.strip().split("|")
        rules.append(a)

 
updates = updates[1:]
 
broken = False
incorrect = []
for update in updates:
    
    for i in range(0,len(update)):
        current = update[i]
        for j in range(i+1,len(update)):
            fvalue = update[j]
            if [fvalue,current] in rules:
                incorrect.append(update)
                broken = True
                break
        if broken:
           break
    broken = False

print(incorrect[0])
print("+++++++++++++++++++++++++++++++++++++++")
 
def fix():
    brok = False
    for u in incorrect:
        for i in range(0,len(u)):
            curr = u[i]
            #print(curr)
            for j in range(i+1,len(u)):
                next = u[j]
                if [next,curr] in rules:
                    x = i
                    while (u[x]!= next):
                        u[x] =  u[x+1]
                        x += 1
                    u[x] = curr
                    brok = True
                    break
            if(brok):
                i = i - 1


           
fix()

print(incorrect[0])
sum = 0
for x in incorrect:
    index = ((len(x)-1)//2)
    
    sum = sum + int(x[index])

print(sum)

 
 

 