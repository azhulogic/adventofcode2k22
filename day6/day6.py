# Alex Zhu
# ADVENT OF CODE 2022
# Day 6

def marker_i_hardly_know_her(fileName):
    """Initial, naive approach for part one"""
    with open(fileName) as f:
        data = f.readline()

        for idx in range(3,len(data)):
            priorRepeats = (data[idx-3] == data[idx-2]) or (data[idx-3] == data[idx-1]) or (data[idx-2] == data[idx-1])
            if data[idx] not in data[idx-3:idx] and not priorRepeats:
                # print(data[idx], data[idx-3:idx])
                return idx + 1

        return -1

def expo_sharpies(fileName):
    """Approach based on using prior searches, offsets by the first of the
    last pair of characters found in a 14-char substring"""
    with open(fileName) as f:
        data = f.readline()

        idx = 0
        while (idx < len(data)-14):
            lastDuplicateIndex = find_last_duplicate(data[idx:idx+14])
            if lastDuplicateIndex == -1:
                # print("found:",data[idx:idx+14])
                return idx + 14
            else:
                idx += lastDuplicateIndex + 1

        return -1


def find_last_duplicate(substring):
    """Helper function for above"""
    lastDuplicateIndex = -1

    for idx in range(len(substring)-1):
        for jdx in range(idx+1,len(substring)):
            if substring[idx] == substring[jdx]:
                # print((substring[idx],substring[jdx]))
                lastDuplicateIndex = idx

    # print("Found pair " + substring[lastDuplicateIndex] + " in: " + substring, " at %d" %lastDuplicateIndex)
    return lastDuplicateIndex


if __name__ == "__main__":
    print("Example One | %d" % marker_i_hardly_know_her("day6/example.txt"))
    print("Part One    | %d" % marker_i_hardly_know_her("day6/input.txt"))
    print("Example Two | %d" % expo_sharpies("day6/example.txt"))
    print("Part One    | %d" % expo_sharpies("day6/input.txt"))