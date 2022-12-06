# Alex Zhu
# ADVENT OF CODE 2022
# Day 5

class CratePuzzle:
    
    def __init__(self,fileName):
        """Constructor, initializes puzzle to be solved"""
        self.labels = []
        self.stacks = []
        self.instructions = []
        crateLists = []

        # parse given file into reasonable data
        # if branches are checked in order of likelihood
        with open(fileName) as f:
            for line in f:
                # check if this is an instruction line (starts with m)
                if line[0] == "m":
                    # store as three element lists of instructions, i.e. [move, from, to]
                    self.instructions.append([int(s) for s in line.split() if s.isdigit()])

                # check if this is a "crate" line
                elif line[0] in [" ","["] and not line[1].isnumeric():
                    # strip unnecessary characters, list of letters or spaces
                    crateLists.append([line[idx] for idx in range(1, len(line), 4)])

                # otherwise is a "label" line (and not the obnoxious empty newline)
                elif line[0] != "\n":
                    # strip spaces, list of string labels
                    self.labels = [line[idx] for idx in range(1, len(line), 4)]
                

            # initialize stacks, see helper function below
            crateLists.reverse()
            self.initialize_stacks(crateLists)

            # uncomment to debug:
            # print(self.labels,crateLists,self.instructions)

    def initialize_stacks(self,crateLists):
        """Helper function, initializes local stacks after data is parsed"""
        stackCount = len(self.labels)
        self.stacks = [[] for _ in range(stackCount)]

        for lst in crateLists:
            for idx in range(stackCount):
                if lst[idx].isalpha():
                    self.stacks[idx].append(lst[idx])

        # print(self.stacks)

    def __str__(self):
        """__str__ method, gives stacks left to right <-> bottom to top"""
        str = ""
        for idx in range(len(self.labels)):
            str += self.labels[idx] + " | [" + "] -> [".join(self.stacks[idx]) + "]\n"

        return str

    def solve(self,craneModel):
        """Driver function for solving problem given crane model"""
        print("BEFORE:\n" + str(self))

        if craneModel == 9000:
            for instr in self.instructions:
                self.execute_instructions_9000(instr)
        else:
            for instr in self.instructions:
                self.execute_instructions_9001(instr)

        print("AFTER:\n" + str(self))
        print("SOLUTION: " + self.get_stack_tops())

    def execute_instructions_9000(self,instr):
        """Helper function for executing line instructions
        takes input of form: [move, from, to]"""
        # repeat "move" amount of times
        for _ in range(instr[0]):
            # pop "from" -> append "to"
            self.stacks[instr[2]-1].append(self.stacks[instr[1]-1].pop())

    def execute_instructions_9001(self,instr):
        """Same premise as above, but pops in groupings"""
        fromStack = self.stacks[instr[1]-1]             # to avoid verbosity
        boxes = fromStack[-instr[0]:]                   # get "move" amt of boxes
        self.stacks[instr[1]-1] = fromStack[:-instr[0]] # remove from "from" stack
        self.stacks[instr[2]-1] += boxes                # concatenate to "to" stack


    def get_stack_tops(self):
        """"Returns the combined string of all top crates"""
        message = ""
        for s in self.stacks:
            message += s[-1]

        return message

if __name__ == "__main__":
    e1 = CratePuzzle("day5/example.txt")
    p1 = CratePuzzle("day5/input.txt")

    print("Example One:")
    e1.solve(9000)
    print("\nPart One")
    p1.solve(9000)

    e2 = CratePuzzle("day5/example.txt")
    p2 = CratePuzzle("day5/input.txt")

    print("Example Two:")
    e2.solve(9001) 
    print("\n Part Two:")
    p2.solve(9001) 
