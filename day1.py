def part1():
    f = open("day1.txt", "r")
    for i in f:
        f1 = open("day1.txt", "r")
        for j in f1:
            if ((int(i) + int(j)) == 2020):
                print(int(i),int(j))
                break
    f.close()
part1()

def part2():
    f = open("day1.txt", "r")
    for i in f:
        f1 = open("day1.txt", "r")
        for j in f1:
            f2 =  open("day1.txt", "r")
            for k in f2:
                if ((int(i) + int(j) + int(k)) == 2020):
                    print(int(i),int(j), int(k))
                    break
    f.close()
part2()