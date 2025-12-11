from collections import defaultdict


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
        N = len(A)

        # Coordinate Compression
        # 0: X (col), 1: Y (row)
        Xs = sorted(list(set(p[0] for p in A)))
        Ys = sorted(list(set(p[1] for p in A)))

        def build_map(coords):
            mapping = {}
            logical = []
            idx = 0
            for i, val in enumerate(coords):
                mapping[val] = idx
                logical.append((val, val))  # Point
                idx += 1
                if i < len(coords) - 1:
                    if coords[i+1] > val + 1:
                        logical.append((val + 1, coords[i+1] - 1))  # Interval
                        idx += 1
            return mapping, logical

        map_x, log_x = build_map(Xs)
        map_y, log_y = build_map(Ys)

        W = len(log_x)
        H = len(log_y)

        # Grid: 1 if valid (Red/Green), 0 otherwise
        grid = [[0] * H for _ in range(W)]

        # 1. Mark Boundary
        for i in range(N):
            p1 = A[i]
            p2 = A[(i + 1) % N]

            x1, y1 = p1
            x2, y2 = p2

            ix1, ix2 = map_x[x1], map_x[x2]
            iy1, iy2 = map_y[y1], map_y[y2]

            for x in range(min(ix1, ix2), max(ix1, ix2) + 1):
                for y in range(min(iy1, iy2), max(iy1, iy2) + 1):
                    grid[x][y] = 1

        # 2. Mark Interior (Parity Scan)
        v_edges = []
        for i in range(N):
            p1 = A[i]
            p2 = A[(i + 1) % N]
            if p1[0] == p2[0]:  # Vertical edge
                x = p1[0]
                y_min = min(p1[1], p2[1])
                y_max = max(p1[1], p2[1])
                v_edges.append((x, y_min, y_max))

        for j in range(H):
            # Scanline at y_check.
            # For Point row, check just above/at the point (y + epsilon behavior)
            # Rule: vertical edge covers if y_min <= y_check < y_max
            y_check = log_y[j][0]

            active_xs = []
            for vx, vymin, vymax in v_edges:
                if vymin <= y_check < vymax:
                    active_xs.append(map_x[vx])

            active_xs.sort()

            for k in range(0, len(active_xs), 2):
                if k+1 < len(active_xs):
                    start_x = active_xs[k]
                    end_x = active_xs[k+1]
                    for x in range(start_x, end_x + 1):
                        grid[x][j] = 1

        # 3. 2D Prefix Sum
        P = [[0] * (H + 1) for _ in range(W + 1)]
        for x in range(W):
            for y in range(H):
                P[x+1][y+1] = P[x][y+1] + P[x+1][y] - P[x][y] + grid[x][y]

        def get_sum(x1, y1, x2, y2):
            return P[x2+1][y2+1] - P[x1][y2+1] - P[x2+1][y1] + P[x1][y1]

        # 4. Check Pairs
        ans = 0
        for i in range(N):
            x1_val, y1_val = A[i]
            ix1, iy1 = map_x[x1_val], map_y[y1_val]

            for j in range(i + 1, N):
                x2_val, y2_val = A[j]
                ix2, iy2 = map_x[x2_val], map_y[y2_val]

                qx1, qx2 = min(ix1, ix2), max(ix1, ix2)
                qy1, qy2 = min(iy1, iy2), max(iy1, iy2)

                total = (qx2 - qx1 + 1) * (qy2 - qy1 + 1)
                valid = get_sum(qx1, qy1, qx2, qy2)

                if valid == total:
                    area = (abs(x1_val - x2_val) + 1) * \
                        (abs(y1_val - y2_val) + 1)
                    if area > ans:
                        ans = area

        return ans


if __name__ == "__main__":
    solver = Solver("input1.txt")
    print(f"Answer 1: {solver.solve1()}")
    print(f"Answer 2: {solver.solve2()}")
