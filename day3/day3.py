# Alex Zhu
# ADVENT OF CODE 2022
# Day 3

def ruck_and_roll(fileName):
    """I wanna ruck and roll all night."""
    with open(fileName) as f:
        sum = 0
        for l in f:
            midpoint = len(l) // 2
            common = list(set(l[:midpoint]).intersection(l[midpoint:]))[0]

            if common.isupper():
                sum += 26 + ord(common) % 64
            else:
                sum += ord(common) % 96

        return sum

def sack_it_to_em(fileName):
    """Sacked like a quarterback"""
    sum = 0
    with open(fileName) as f:
        for l1,l2,l3 in zip(*[iter(f)]*3):
            common = set(l1[:-1]).intersection(l2[:-1])     # remove newlines
            common = list(common.intersection(l3[:-1]))[0]
        
            if common.isupper():
                sum += 26 + ord(common) % 64
            else:
                sum += ord(common) % 96
    return sum

if __name__ == "__main__":
    print("Example One | %d" % ruck_and_roll("day3/example.txt"))
    print("Part One    | %d" % ruck_and_roll("day3/input.txt"))
    print("Example Two | %d" % sack_it_to_em("day3/example.txt"))
    print("Part Two    | %d" % sack_it_to_em("day3/input.txt"))