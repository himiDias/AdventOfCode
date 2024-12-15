inp = open("Day8/input8.txt")

grid = []
grid_an = []
for line in inp:
    line = list(line.strip())
    linec = line[:]
    grid.append(line)
    grid_an.append(linec)

antennas = []
for y in range(0,len(grid)):
    yl = grid[y]
    for x in range(0,len(yl)):
        if yl[x] != '.' and yl[x] not in antennas:
            antennas.append(yl[x])


print(antennas)
count = 0
for a in antennas:
    for y in range(0,len(grid)):
        yl = grid[y]
        for x in range(0,len(yl)):
            if yl[x] == a:
                count += 1
                curr_y = y
                curr_x = x
                for j in range(0,len(grid)):
                    jl = grid[j]
                    for i in range(0,len(jl)):
                        if jl[i] == a and i != curr_x and j != curr_y:
                            add_y = (curr_y - j)*2
                            add_x = (curr_x - i)*2
                            if add_y < 0:
                                new_y = curr_y + abs(add_y)
                                if (add_x < 0):
                                    new_x = curr_x + abs(add_x)
                                    while (new_y < len(grid) and new_x<len(jl)):
                                        grid_an[new_y][new_x]='#'
                                        new_y = new_y + abs(add_y)//2
                                        new_x = new_x + abs(add_x)//2
                                else:
                                    new_x = curr_x - abs(add_x)
                                    while (new_y < len(grid) and new_x>=0):
                                        grid_an[new_y][new_x]='#'
                                        new_y = new_y + abs(add_y)//2
                                        new_x = new_x - abs(add_x)//2
                            else:
                                new_y = curr_y - abs(add_y)
                                if (new_y >= 0):
                                    if (add_x < 0):
                                        new_x = curr_x + abs(add_x)
                                        while (new_y >= 0  and new_x<len(jl)):
                                            grid_an[new_y][new_x]='#'
                                            new_y = new_y - abs(add_y)//2
                                            new_x = new_x + abs(add_x)//2
                                    else:
                                        new_x = curr_x - abs(add_x)
                                        while (new_y >= 0 and new_x>=0):
                                            grid_an[new_y][new_x]='#'
                                            new_y = new_y - abs(add_y)//2
                                            new_x = new_x - abs(add_x)//2



for i in range(0,len(grid_an)):
    il = grid_an[i]
    for j in range(0,len(il)):
        if il[j] == '#' and grid[i][j]=='.':
            count +=1

for i in grid_an:
    print (''.join(i))
print(count)
