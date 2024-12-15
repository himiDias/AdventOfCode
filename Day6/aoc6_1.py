inp = open("Day6/input6.txt")

grid = []
for line in inp:
    line = list(line.strip())
    grid.append(line)


#print(grid)

brok = False
for y in range(0,len(grid)):
    for x in range(0,len(grid[y])):
        if grid[y][x] == "^":
            pos_x = x
            pos_y = y
            dir = "^"
            brok = True
            break
    if brok:
        break

save_posy = pos_y
save_posx = pos_x

while True:
    if dir == "^":
        if pos_y -1 < 0:
            grid[pos_y][pos_x] = "X"
            break
        if grid[pos_y-1][pos_x]=="#":
            dir = ">"
        else:
            grid[pos_y][pos_x] = "X"
            pos_y -= 1
    elif dir == ">":
        if pos_x +1 >= len(grid[pos_y]):
            grid[pos_y][pos_x] = "X"
            break
        if grid[pos_y][pos_x+1]=="#":
            dir = "v"
        else:
            grid[pos_y][pos_x] = "X"
            pos_x += 1
    elif dir == "v":
        if pos_y + 1 >= len(grid):
            grid[pos_y][pos_x] = "X"
            break
        if grid[pos_y+1][pos_x]=="#":
            dir = "<"
        else:
            grid[pos_y][pos_x] = "X"
            pos_y += 1
    else:
        if pos_x - 1 < 0:
            grid[pos_y][pos_x] = "X"
            break
        if grid[pos_y][pos_x-1]=="#":
            dir = "^"
        else:
            grid[pos_y][pos_x] = "X"
            pos_x -= 1




 