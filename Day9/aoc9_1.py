inp = open("Day9/test9.txt")

for line in inp:
    li = line.strip()
print(li)

block = True
fmt_li = ""
id = 0 
for i in li:
    if(block):
        fmt_li = fmt_li + (str(id)*int(i))
        id += 1
        block = False
    else:
        fmt_li = fmt_li + ('.'*int(i))
        block = True

fmt_list = list(fmt_li)

print("".join(fmt_list))

lPtr = 0
rPtr = len(fmt_list)-1
while True:
    if fmt_list[rPtr] != '.':
        while fmt_list[lPtr] != '.' and lPtr<len(fmt_list):
            lPtr += 1
        
        if(lPtr <= rPtr):
            fmt_list[lPtr] = fmt_list[rPtr]
            fmt_list[rPtr] = '.'
    rPtr -= 1
    if (lPtr >= rPtr):
        break

checksum =0

for i in range(0,len(fmt_list)):
    if (fmt_list[i]=="."):
        break
    checksum = checksum + int(fmt_list[i])*i

print(''.join(fmt_list))
print(checksum)

