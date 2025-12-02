INPUT = "10327-17387,74025-113072,79725385-79874177,964628-1052240,148-297,3-16,126979-227778,1601-2998,784-1207,831289-917268,55603410-55624466,317-692,602197-750430,17-32,38-58,362012-455626,3622441-3647505,883848601-883920224,62-105,766880-804855,9184965756-9185005415,490073-570277,2929273115-2929318135,23251-48475,9696863768-9697013088,229453-357173,29283366-29304416,4526-8370,3095-4389,4400617-4493438"
# INPUT = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

class Solver:
    def __init__(self, input):
        self.input = input

    def solve1(self):
        ranges = self.input.split(',')
        ans = 0
        for r in ranges:
            start, end = map(int, r.split('-'))
            for x in range(start, end + 1):
                x = str(x)
                if len(x) % 2 == 0 and x[:len(x)//2] == x[len(x)//2:]:
                    ans += int(x)

        return ans
    
    def solve2(self):
        ranges = self.input.split(',')
        ans = 0
        for r in ranges:
            start, end = map(int, r.split('-'))

            for t in range(start, end + 1):
                x = str(t)
                for k in range(1, len(x)//2 + 1):
                    if len(x) % k == 0:
                        ok = True
                        base = x[:k]

                        for i in range(k, len(x), k):
                            if base != x[i:i+k]:
                                ok = False
                                break

                        if ok:
                            ans += t
                            break

        return ans

if __name__ == "__main__":
    solver = Solver(INPUT)
    print(f"Answer 1: {solver.solve1()}")
    print(f"Answer 2: {solver.solve2()}")