# Alex Zhu
# ADVENT OF CODE 2022
# Day 4

def ranger_danger(fileName,full):
    count = 0
    with open(fileName) as f:
        for line in f:
            [a,b] = line.split(",")
            [c,d] = a.split("-")
            [e,f] = b.split("-")

            c = int(c)
            d = int(d)
            e = int(e)
            f = int(f)

            # handle full overlap
            if full and ((c >= e and d <= f) or (c <= e and d >= f)):
                count += 1
            # handle partial overlap
            elif not full and (c <= e and e <= d) or (e <= c and c <= f):
                count += 1
    return count

if __name__ == "__main__":
    print("Example One | %d" % ranger_danger("day4/example.txt",True))
    print("Part One    | %d" % ranger_danger("day4/input.txt",True))
    print("Example Two | %d" % ranger_danger("day4/example.txt",False))
    print("Part Two    | %d" % ranger_danger("day4/input.txt",False))