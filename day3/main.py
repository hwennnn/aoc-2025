class Solver:
    def __init__(self, input_file):
        self.input_file = input_file
    
    def parse_inputs(self):
        with open(self.input_file, 'r') as file:
            data = file.readlines()
            for line in data:
                yield line.strip()

    def solve1(self):
        inputs = self.parse_inputs()
        ans = 0
        
        for line in inputs:
            N = len(line)
            mmax = 0
            for i in range(N):
                a = int(line[i])
                for j in range(i + 1, N):
                    b = int(line[j])
                    curr = a * 10 + b
                    if curr > mmax:
                        mmax = curr

            ans += mmax

        return ans
    
    def solve2(self):
        instructions = self.parse_inputs()
        ans = 0
     
                    
        return ans

if __name__ == "__main__":
    solver = Solver("input2.txt")
    print(f"Answer 1: {solver.solve1()}")
    print(f"Answer 2: {solver.solve2()}")