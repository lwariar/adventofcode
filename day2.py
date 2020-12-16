def part1():
    f = open("day2.txt", "r")
    total = 0
    for line in f:
        minmax, letter, pwd = line.split(' ')
        min, max = minmax.split('-')
        letter = letter.strip(':')
        count = 0
        for i in pwd:
            if i == letter:
                count += 1
        if count == 0 or count < int(min) or count > int(max):
            continue
        else: 
            total += 1
    return total
    f.close()

print(part1())

def part2():
    f = open("day2.txt", "r")
    count = 0
    for line in f:
        position, letter, pwd = line.split(' ')
        first, next = position.split('-')
        letter = letter.strip(':')
        if (pwd[int(first)-1] == letter and pwd[int(next)-1] != letter) or (pwd[int(first)-1] != letter and pwd[int(next)-1] == letter):
                count += 1
    return count
    f.close()

print(part2())