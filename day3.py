def part1():
    f = open("day3.txt", "r")
    trees = 0
    layout = []
    #follow a slope of right 3 and down 1
    for line in f:
        layout.append(line.strip('\n'))

    for i in range(0, len(layout)):
        if i > 0:
            position = layout[i][(i*3) % len(layout[0])]
            if position == '#':
                trees += 1
    return trees
    f.close()

print(part1())


