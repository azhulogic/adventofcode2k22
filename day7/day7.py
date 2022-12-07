# Alex Zhu
# ADVENT OF CODE 2022
# Day 7

class FileTree:
    """file system as a tree data structure using dicts"""

    def __init__(self,parent,data,name) -> None:
        self.children = {}      # {name : node} pairs
        self.parent = parent    # points to parent node (for backtracking)
        self.data = int(data)   # int value
        self.name = name        # name of directory

    def __str__(self) -> str:
        return self.strBuilder(0)

    def strBuilder(self,depth) -> str:
        """helper function for __str__. Indents based on depth"""
        retstr = "  " * depth
        if len(self.children):
            retstr += "- " + self.name + " (dir)" + "\n"
            for c in self.children.values():
                retstr += c.strBuilder(depth+1)
        else:
            retstr += "- " + self.name + " (file, size=" + str(self.data) + ")\n"

        return retstr

    def addChild(self,name,data) -> None:
        """add a child with data to the tree"""
        self.children[name] = FileTree(self,data,name)

    def getSize(self) -> int:
        """recursively gets size of tree"""
        return self.data + sum([x.getSize() for x in self.children.values()])

def read_commands(fileName) -> FileTree:
    """parse input commands, return resulting file system"""
    currentDir = FileTree(None,0,"/")
    root = currentDir

    with open(fileName) as f:
        for line in f:
            # get rid of newlines, and turn into str lists
            parsed = line.strip().split(" ") 

            # is a command
            if parsed[0] == "$":
                match parsed[1]:
                    case "cd":
                        # move up a directory
                        if parsed[2] == "..":
                            currentDir = currentDir.parent
                        # return to root
                        elif parsed[2] == "/":
                            currentDir = root 
                        # move down a directory
                        else:
                            currentDir = currentDir.children[parsed[2]]
                    case "ls":
                        pass # handled below

            # is a directory
            elif parsed[0] == "dir":
                currentDir.addChild(parsed[1],0)

            # is a file (i.e. a leaf node)
            else:
                currentDir.addChild(parsed[1],parsed[0])

    return root

def get_directory_sizes(tree):
    """get directory sizes, returns a formatted string and a tuple list containing
    all directory sizes of given tree"""
    retstr = ""
    retdict = []

    if not tree.data:
        name = tree.name
        size = tree.getSize()

        retstr = "dir " + name + " has size " + str(size) + "\n"
        retdict.append((name,size))
        for c in tree.children.values():
            s,l = get_directory_sizes(c)
            retstr += s
            retdict += l

    return retstr, retdict

def find_viable_directory(sizes,spaceNeeded):
    """find smallest viable directory to delete given space needed.
    Uses the tuple list given by get_directory_sizes()"""
    minimumSize = sizes[0][1] - spaceNeeded
    currentSize = spaceNeeded

    for _,size in sizes:
        if size > minimumSize and size < currentSize:
            currentSize = size

    return currentSize

if __name__ == "__main__":
    fileSystem = read_commands("day7/example.txt")
    s,l = get_directory_sizes(fileSystem)
    # print(fileSystem)
    # print(s)
    print("Example One | %d" % sum([size for _,size in l if size <= 100_000]))
    print("Example Two | %d" % find_viable_directory(l,40_000_000))

    fileSystem = read_commands("day7/input.txt")
    s,l = get_directory_sizes(fileSystem)
    # print(fileSystem)
    # print(s)
    print("Input One   | %d" % sum([size for _,size in l if size <= 100_000]))
    print("Input Two   | %d" % find_viable_directory(l,40_000_000))


