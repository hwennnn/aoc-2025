class Solver:
    def __init__(self, input_file):
        self.input_file = input_file

    def parse_inputs(self):
        A = []

        with open(self.input_file, 'r') as file:
            data = file.readlines()
            for line in data:
                A.append(list(line.strip()))

        return A

    def solve1(self):
        A = self.parse_inputs()
        rows, cols = len(A), len(A[0])
        ans = 0
        curr = set()
        start = None

        for i in range(rows):
            for j in range(cols):
                if A[i][j] == 'S':
                    start = (i, j)
                    curr.add(j)
                    break

            if start is not None:
                break

        if start is None:
            return 0

        si, _ = start
        for i in range(si, rows):
            next_curr = set()

            for j in curr:
                if j < 0 or j >= cols:
                    continue

                if A[i][j] == '^':
                    ans += 1
                    next_curr.add(j - 1)
                    next_curr.add(j + 1)
                else:
                    next_curr.add(j)

            curr = next_curr
            if not curr:
                break

        return ans

    def solve2(self):
        A = self.parse_inputs()
        ans = 0

        return ans


if __name__ == "__main__":
    solver = Solver("input2.txt")
    print(f"Answer 1: {solver.solve1()}")
    print(f"Answer 2: {solver.solve2()}")
