import re

def checkUp(x,y):
    if y-3 < 0:
        return False
     
    if (grid[y-1][x] == "M" and grid[y-2][x] == "A" and grid[y-3][x] == "S"):
        return True
    else:
        return False

def checkDown(x,y):
    if y+3 >= len(grid):
        return False
    
    if (grid[y+1][x] == "M" and grid[y+2][x] == "A" and grid[y+3][x] == "S"):
        return True
    else:
        return False


def checkUR(x,y,length):
    if y-3 < 0 or x + 3 >= length:
        return False
    
    if (grid[y-1][x+1] == "M" and grid[y-2][x+2] == "A" and grid[y-3][x+3] == "S"):
        return True
    else:
        return False
    
def checkUL(x,y):
    if y-3 < 0 or x - 3 < 0:
        return False
    if (grid[y-1][x-1] == "M" and grid[y-2][x-2] == "A" and grid[y-3][x-3] == "S"):
        return True
    else:
        return False
    
def checkDR(x,y,length):
    if y+3 >= len(grid) or x + 3 >= length:
        return False
    
    if (grid[y+1][x+1] == "M" and grid[y+2][x+2] == "A" and grid[y+3][x+3] == "S"):
        return True
    else:
        return False

def checkDL(x,y):
    if y+3 >= len(grid) or x - 3 < 0:
        return False
    if (grid[y+1][x-1] == "M" and grid[y+2][x-2] == "A" and grid[y+3][x-3] == "S"):
        return True
    else:
        return False

inp = open("Day4/input4.txt")

 
grid = []
count = 0
y = 0
for line in inp:
    grid.append(line.strip())
    regR = re.findall("XMAS",line)
    regL = re.findall("SAMX",line)
    count = count + len(regL)+len(regR)

for line in grid:
    length = len(line)
    for x in range(0,length):
        if line[x] == "X":
            if (checkUp(x,y)):
                count = count + 1
                print("up",x,y)
            if (checkDown(x,y)):
                count = count + 1
                print("dw",x,y)
            if (checkUR(x,y,length)):
                count = count + 1
                print("ur",x,y)
            if (checkUL(x,y)):
                count = count + 1
                print("ul",x,y)
            if (checkDR(x,y,length)):
                count = count + 1
                print("dr",x,y)
            if (checkDL(x,y)):
                count = count + 1
                print("dl",x,y)

    y = y + 1

 
print(count)

 