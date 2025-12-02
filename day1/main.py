class Solver:
    def __init__(self, input_file):
        self.input_file = input_file
    
    def parse_instructions(self):
        with open(self.input_file, 'r') as file:
            data = file.readlines()
            for line in data:
                yield line.strip()

    def solve1(self):
        instructions = self.parse_instructions()
        ans = 0
        curr = 50

        for instruction in instructions:
            if instruction[0] == 'R':
                curr = (curr + int(instruction[1:]) + 100) % 100
            else:
                curr = (curr - int(instruction[1:]) + 100) % 100
            
            if curr == 0:
                ans += 1

        return ans
    
    def solve2(self):
        instructions = self.parse_instructions()
        ans = 0
        curr = 50

        for instruction in instructions:
            d = 1 if instruction[0] == 'R' else -1

            for _ in range(int(instruction[1:])):
                curr = (curr + d + 100) % 100
                if curr == 0:
                    ans += 1
                    
        return ans

if __name__ == "__main__":
    solver = Solver("input.txt")
    print(f"Answer 1: {solver.solve1()}")
    print(f"Answer 2: {solver.solve2()}")