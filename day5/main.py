from collections import defaultdict, deque


class Solver:
    def __init__(self, input_file):
        self.input_file = input_file

    def parse_inputs(self):
        ranges = []
        A = []
        curr = ranges

        with open(self.input_file, 'r') as file:
            data = file.readlines()
            for line in data:
                if line == "\n":
                    curr = A
                    continue
                curr.append(line.strip())

        return ranges, A

    def solve1(self):
        ranges, A = self.parse_inputs()
        A = list(map(int, A))
        ans = 0
        flags = []

        for r in ranges:
            start, end = map(int, r.split('-'))
            flags.append((1, start))
            flags.append((0, end + 1))

        for x in A:
            flags.append((2, x))

        flags.sort(key=lambda x: (x[1], x[0]))

        curr = 0
        for f, x in flags:
            if f == 0:
                curr -= 1
            elif f == 1:
                curr += 1
            else:
                if curr >= 1:
                    ans += 1

        return ans

    def solve2(self):
        ranges, A = self.parse_inputs()

        ans = 0

        return ans


if __name__ == "__main__":
    solver = Solver("input2.txt")
    print(f"Answer 1: {solver.solve1()}")
    print(f"Answer 2: {solver.solve2()}")
