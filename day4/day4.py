def pair_of_balls(fileName):
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

            if (c >= e and d <= f) or (c <= e and d >= f):
                count += 1
    return count

if __name__ == "__main__":
    print(pair_of_balls("day4/input.txt"))