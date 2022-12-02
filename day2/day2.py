# Alex Zhu
# ADVENT OF CODE 2022
# Day 2

def rock_paper_scissors(fileName):
    """Do you dare try to figure out what I wrote? O(n)"""
    return sum(list(map(lambda s : (ord(s[2])-ord(s[0])+2) % 3 * 3 + (ord(s[2]) + 1) % 4, open(fileName))))

def scissors_paper_rock(fileName):
    """Okay, coding like a normal person. Kind of."""
    score = 0
    with open(fileName) as f:
        for l in f:
            elf_play = ord(l[0]) - 65 # {0,1,2} : rock paper scissors
            you_play = ord(l[2]) - 88 # {0,1,2} : lose, draw, win

            score += (elf_play + you_play - 1) % 3 + 1 + you_play * 3
    return score

if __name__ == "__main__":
    print("Example P1 | %d" % rock_paper_scissors("day2/example.txt"))
    print("Input P1   | %d" % rock_paper_scissors("day2/input.txt"))
    print("Example P2 | %d" % scissors_paper_rock("day2/example.txt"))
    print("Input P2   | %d" % scissors_paper_rock("day2/input.txt"))