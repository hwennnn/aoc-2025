class Solver:
    def __init__(self, input_file):
        self.input_file = input_file

    def parse_inputs(self):
        points = []
        with open(self.input_file, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = list(map(int, line.split(',')))
                points.append(tuple(parts))
        return points

    def solve1(self):
        A = self.parse_inputs()
        N = len(A)
        ans = 0

        for i in range(N):
            y1, x1 = A[i]
            for j in range(i + 1, N):
                y2, x2 = A[j]
                ans = max(ans, abs(y1 - y2 + 1) * abs(x1 - x2 + 1))

        return ans

    def solve2(self):
        A = self.parse_inputs()
        ans = 0
        return 0


if __name__ == "__main__":
    solver = Solver("input2.txt")
    print(f"Answer 1: {solver.solve1()}")
    print(f"Answer 2: {solver.solve2()}")
