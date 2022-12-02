# Alex Zhu
# ADVENT OF CODE 2022
# Day 1

def caloric_consumer(fileName):
    """Counts calories of elves or something, makes me hungry. O(n)"""
    calories = 0
    counts = []

    with open(fileName) as f:
        for line in f:
            if line == "\n":
                counts.append(calories)
                calories = 0
            else:
                calories += int(line)

    return counts
    
def konsumption_kings(counts):
    """Despite two for loops? Actually still O(n), maybe amortized."""
    maxima = [0,0,0]

    for calories in counts:
        for idx in range(len(maxima)):
            if calories > maxima[idx]:
                maxima.insert(idx, calories)
                maxima.pop()
                break

    return sum(maxima)

if __name__ == "__main__":
    counts = caloric_consumer("day1\example.txt")
    print("Example  | Max calorie count: %d" % max(counts))
    counts = caloric_consumer("day1\partone.txt")
    print("Part One | Max calorie count: %d" % max(counts))
    max = konsumption_kings(counts)
    print("Part Two | Top three calorie count: %d" % max)