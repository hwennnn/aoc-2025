from collections import defaultdict, deque


class Solver:
    def __init__(self, input_file):
        self.input_file = input_file

    def parse_inputs(self):
        A = []

        with open(self.input_file, 'r') as file:
            data = file.readlines()
            for line in data:
                A.append(line.strip().split())

        return A

    def solve1(self):
        A = self.parse_inputs()
        rows, cols = len(A), len(A[0])
        ans = 0

        for j in range(cols):
            op = A[-1][j]
            if op == '*':
                curr = 1
                for i in range(rows - 1):
                    curr *= int(A[i][j])
            else:
                curr = sum(int(A[i][j]) for i in range(rows - 1))
            ans += curr

        return ans

    def parse_grid(self):
        with open(self.input_file, 'r') as file:
            lines = [line.rstrip('\n') for line in file]

        max_len = max(len(line) for line in lines)
        grid = [line.ljust(max_len) for line in lines]
        return grid

    def solve2(self):
        A = self.parse_grid()
        rows, cols = len(A), len(A[0])
        ans = 0

        problems = []
        current_group = []

        for j in range(cols):
            col_chars = [A[i][j] for i in range(rows)]
            is_separator = all(c == ' ' for c in col_chars)

            if is_separator:
                if current_group:
                    problems.append(current_group)
                    current_group = []
            else:
                current_group.append(col_chars)

        if current_group:
            problems.append(current_group)

        for problem in problems:
            op = None
            numbers = []

            for col in problem:
                if col[-1] in ('+', '*'):
                    op = col[-1]

                digit_chars = col[:-1]
                num_str = "".join(digit_chars).replace(" ", "")

                if num_str:
                    numbers.append(int(num_str))

            if not op:
                continue

            if op == '+':
                val = sum(numbers)
            elif op == '*':
                val = 1
                for n in numbers:
                    val *= n

            ans += val

        return ans


if __name__ == "__main__":
    solver = Solver("input2.txt")
    print(f"Answer 1: {solver.solve1()}")
    print(f"Answer 2: {solver.solve2()}")
