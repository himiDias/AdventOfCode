inp = open("Day5/input5.txt")
 
rules = []
updates = []
flag = False
for line in inp:
    if line == "\n":
        flag = True
    
    if (flag):
        a = line.strip().split(",")
        #print(a)
        updates.append(a)
    else:
        a = line.strip().split("|")
        rules.append(a)

#print(rules)
updates = updates[1:]
#print(updates)
broken = False
correct = []
for update in updates:
    #print(update)
    for i in range(0,len(update)):
        current = update[i]
        for j in range(i+1,len(update)):
            fvalue = update[j]
            #print(fvalue)
            #print([fvalue,current])
            if [fvalue,current] in rules:
                #print("rule broken")
                #print("Rule",fvalue,current)
                broken = True
                break
        if broken:
           break
    if (not broken):
        correct.append(update)
    broken = False

#print(correct)

sum = 0
for x in correct:
    index = ((len(x)-1)//2)
    print(index)
    sum = sum + int(x[index])

print(sum)