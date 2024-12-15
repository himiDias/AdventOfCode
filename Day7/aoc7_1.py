inp = open("Day7/input7.txt")

sum = 0
for line in inp:
    line = line.strip().split(":")
    line[0] = int(line[0])
    line[1] = list(map(int,line[1].split()))

    ans = line[0]
    vals = line[1]
    spaces = len(line[1]) - 1

    c = 0
    while c < 2**spaces:
        bin_c = "{0:b}".format(c)
        #print(bin_c)
        a = vals[0]
        #print("A , start val", a)
        for i in range(1,len(vals)):
            if (i-1) >= len(bin_c) or bin_c[(len(bin_c)-i)]=="0":
                a = a + vals[i]
            else:
                if (a==0):
                    a = 1
                a = a * vals[i]
            #print("Runtime a :",a)
        #print("A" ,a,"Val",ans)
        #print(a)
        if (a == ans):
            sum = sum + ans
            break
        c += 1


print("Sum: ",sum)
    


   
  