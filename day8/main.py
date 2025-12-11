class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
            return True
        return False


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
        points = self.parse_inputs()

        limit = 10 if len(points) <= 20 else 1000

        edges = []
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                p1 = points[i]
                p2 = points[j]
                dist_sq = (p1[0]-p2[0])**2 + \
                    (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2
                edges.append((dist_sq, i, j))

        # Sort by distance 
        edges.sort(key=lambda x: x[0])

        dsu = DSU(n)

        # Process the closest pairs
        count = 0
        for _, u, v in edges:
            if count >= limit:
                break

            dsu.union(u, v)
            count += 1

        # Get component sizes
        component_sizes = []
        visited_roots = set()
        for i in range(n):
            root = dsu.find(i)
            if root not in visited_roots:
                visited_roots.add(root)
                component_sizes.append(dsu.size[root])

        component_sizes.sort(reverse=True)

        # Edge case if fewer than 3 circuits
        if len(component_sizes) < 3:
            ans = 1
            for s in component_sizes:
                ans *= s
            return ans

        ans = component_sizes[0] * component_sizes[1] * component_sizes[2]
        return ans

    def solve2(self):
        points = self.parse_inputs()

        edges = []
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                p1 = points[i]
                p2 = points[j]
                dist_sq = (p1[0]-p2[0])**2 + \
                    (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2
                edges.append((dist_sq, i, j))

        edges.sort(key=lambda x: x[0])

        dsu = DSU(n)
        components = n

        for _, u, v in edges:
            if dsu.union(u, v):
                components -= 1
                if components == 1:
                    p1 = points[u]
                    p2 = points[v]
                    return p1[0] * p2[0]
        return 0


if __name__ == "__main__":
    solver = Solver("input1.txt")
    print(f"Answer 1: {solver.solve1()}")
    print(f"Answer 2: {solver.solve2()}")
