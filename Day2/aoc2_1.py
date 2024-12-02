inp = open("Day2/input2.txt")

safe_count = 0

for line in inp:
    arr = list(map(int,line.strip().split()))
 #   print(arr)
    flag = True
    if (arr[0]<arr[1]):
        #increasing
        for i in range(1,len(arr)):
            if (arr[i-1] >= arr[i] or arr[i]-arr[i-1]>3):
                flag = False
                break
        if flag:
            safe_count = safe_count + 1
    elif (arr[0]>arr[1]):
        #decreasing
        for i in range(1,len(arr)):
            if (arr[i-1]<=arr[i] or arr[i-1]-arr[i]>3):
                flag = False
                break
        if flag:
            safe_count = safe_count + 1   

    else:
        #equals so not safe
        pass




 

print(safe_count)