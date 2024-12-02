inp = open("Day2/input2.txt")

safe_count = 0

for line in inp:
    arr = line.split(" ")
    print(arr)
     
    st = int(arr[0])
    for i in range (1,len(arr)):
        if int(arr[i])