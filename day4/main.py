from collections import defaultdict, deque


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
        grid = [line for line in inputs]
        ans = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '@':
                    count = 0
                    for di in range(-1, 2):
                        for dj in range(-1, 2):
                            if 0 <= i + di < len(grid) and 0 <= j + dj < len(grid[i]):
                                if grid[i + di][j + dj] == '@':
                                    count += 1

                    if count <= 4:
                        ans += 1

        return ans

    def solve2(self):
        inputs = self.parse_inputs()
        grid = [list(line) for line in inputs]
        ans = 0

        while True:
            curr = 0
            marked = []

            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] == '@':
                        count = 0
                        for di in range(-1, 2):
                            for dj in range(-1, 2):
                                if 0 <= i + di < len(grid) and 0 <= j + dj < len(grid[i]):
                                    if grid[i + di][j + dj] == '@':
                                        count += 1

                        if count <= 4:
                            marked.append((i, j))
                            curr += 1

            if curr == 0:
                break

            for i, j in marked:
                grid[i][j] = '.'

            ans += curr

        return ans

    def toposort(self):
        inputs = self.parse_inputs()
        grid = [list(line) for line in inputs]
        graph = defaultdict(set)
        ans = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '@':
                    for di in range(-1, 2):
                        for dj in range(-1, 2):
                            if 0 <= i + di < len(grid) and 0 <= j + dj < len(grid[i]):
                                if grid[i + di][j + dj] == '@':
                                    graph[(i, j)].add((i + di, j + dj))
                                    graph[(i + di, j + dj)].add((i, j))

        queue = deque()
        visited = set()

        for i, j in graph.keys():
            if len(graph[(i, j)]) <= 4:
                visited.add((i, j))
                queue.append((i, j))

        while queue:
            new_queue = deque()

            for _ in range(len(queue)):
                i, j = queue.popleft()
                ans += 1

                for ni, nj in graph[(i, j)]:
                    if (ni, nj) not in visited:
                        graph[(ni, nj)].discard((i, j))
                        if len(graph[(ni, nj)]) <= 4:
                            visited.add((ni, nj))
                            new_queue.append((ni, nj))

            queue = new_queue

        return ans


if __name__ == "__main__":
    solver = Solver("input2.txt")
    print(f"Answer 1: {solver.solve1()}")
    print(f"Answer 2: {solver.solve2()}")
    print(f"Answer 2 (with toposort): {solver.toposort()}")
