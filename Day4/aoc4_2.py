import re


def checkX(x,y,length):
    if y + 1 >=len(grid) or y - 1 < 0 or x + 1 >= length or x-1 <0:
        return False
    
    if (grid[y-1][x-1] == "M" and grid[y+1][x-1] == "M" and grid[y-1][x+1] == "S" and grid[y+1][x+1] == "S"):
        return True
    elif (grid[y-1][x-1] == "S" and grid[y+1][x-1] == "S" and grid[y-1][x+1] == "M" and grid[y+1][x+1] == "M"):
        return True
    elif (grid[y-1][x-1] == "S" and grid[y+1][x-1] == "M" and grid[y-1][x+1] == "S" and grid[y+1][x+1] == "M"):
        return True
    elif (grid[y-1][x-1] == "M" and grid[y+1][x-1] == "S" and grid[y-1][x+1] == "M" and grid[y+1][x+1] == "S"):
        return True
    else:
        return False

 
    


inp = open("Day4/input4.txt")

 
grid = []
count = 0
y = 0
for line in inp:
    grid.append(line.strip())

for line in grid:
    length = len(line)
    for x in range(0,length):
        if line[x] == "A":
            if (checkX(x,y,length)):
                count = count+1

    y = y + 1

 
print(count)
