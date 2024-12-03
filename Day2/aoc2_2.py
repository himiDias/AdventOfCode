inp = open("Day2/input2.txt")

def safe_check(arr):
    if (arr[0]<arr[1]):
        #increasing
        for i in range(1,len(arr)):
            if (arr[i-1] >= arr[i] or arr[i]-arr[i-1]>3):
                return False
        return True
    elif (arr[0]>arr[1]):
        #decreasing
        for i in range(1,len(arr)):
            if (arr[i-1]<=arr[i] or arr[i-1]-arr[i]>3):
                return False
        return True

    else:
        #equals so not safe
        return False

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
        else:
            #print(arr)
            for i in range(0,len(arr)):
                if i == len(arr) - 1:
                    array = arr[:i]
                else:
                    array = arr[:i] + arr[i+1:]
                #print(array)
                if(safe_check(array)):
                    safe_count = safe_count + 1
                    break
    elif (arr[0]>arr[1]):
        #decreasing
        for i in range(1,len(arr)):
            if (arr[i-1]<=arr[i] or arr[i-1]-arr[i]>3):
                flag = False
                break
        if flag:
            safe_count = safe_count + 1   
        else:
            print(arr)
            for i in range(0,len(arr)):
                if i == len(arr) - 1:
                    array = arr[:i]
                else:
                    array = arr[:i] + arr[i+1:]
                print(array)
                if(safe_check(array)):
                    safe_count = safe_count + 1
                    break

    else:
        for i in range(0,len(arr)):
                if i == len(arr) - 1:
                    array = arr[:i]
                else:
                    array = arr[:i] + arr[i+1:]
                print(array)
                if(safe_check(array)):
                    safe_count = safe_count + 1
                    break


 

print(safe_count)