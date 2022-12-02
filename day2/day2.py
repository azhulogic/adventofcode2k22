# Alex Zhu
# ADVENT OF CODE 2022
# Day 2


def rock_paper_scissors(fileName):
    """Do you dare try to figure out what I wrote? O(n)"""
    score = [3,0,6]
    with open(fileName) as f:
        return sum(list(map(lambda s: score[(((ord(s[0]) - 61) - (ord(s[2]) - 87)) % 3)] + (ord(s[2]) - 87), f)))


if __name__ == "__main__":
    print(rock_paper_scissors("day2/example.txt"))