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

for a in antennas:
    for y in range(0,len(grid)):
        yl = grid[y]
        for x in range(0,len(yl)):
            if yl[x] == a:
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
                                if (new_y < len(grid)):
                                    if add_x < 0:
                                        new_x = curr_x + abs(add_x)
                                        if (new_x<len(jl)):
                                            grid_an[new_y][new_x] = '#'
                                    else:
                                        new_x = curr_x - abs(add_x)
                                        if (new_x>=0):
                                            grid_an[new_y][new_x] = '#'
                            else:
                                new_y = curr_y - abs(add_y)
                                if (new_y >= 0):
                                    if add_x < 0:
                                        new_x = curr_x + abs(add_x)
                                        if (new_x<len(jl)):
                                            grid_an[new_y][new_x] = '#'
                                    else:
                                        new_x = curr_x - abs(add_x)
                                        if (new_x>=0):
                                            grid_an[new_y][new_x] = '#'
count = 0
for i in grid_an:
    for j in i:
        if j == '#':
            count += 1
for i in grid_an:
    print (''.join(i))
print(count)
