from typing import List

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ones = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1]

        def rect_area(points):
            if not points:
                return float("inf")
            r1, r2 = min(p[0] for p in points), max(p[0] for p in points)
            c1, c2 = min(p[1] for p in points), max(p[1] for p in points)
            return (r2 - r1 + 1) * (c2 - c1 + 1)

        best = float("inf")

        # Case 1: Split by rows into 3 parts
        for r1 in range(m - 2):
            for r2 in range(r1 + 1, m - 1):
                group1 = [(i, j) for (i, j) in ones if i <= r1]
                group2 = [(i, j) for (i, j) in ones if r1 < i <= r2]
                group3 = [(i, j) for (i, j) in ones if i > r2]
                best = min(best, rect_area(group1) + rect_area(group2) + rect_area(group3))

        # Case 2: Split by cols into 3 parts
        for c1 in range(n - 2):
            for c2 in range(c1 + 1, n - 1):
                group1 = [(i, j) for (i, j) in ones if j <= c1]
                group2 = [(i, j) for (i, j) in ones if c1 < j <= c2]
                group3 = [(i, j) for (i, j) in ones if j > c2]
                best = min(best, rect_area(group1) + rect_area(group2) + rect_area(group3))

        # Case 3: Split as 1 horizontal, then each half split vertically
        for r in range(m - 1):
            top = [(i, j) for (i, j) in ones if i <= r]
            bottom = [(i, j) for (i, j) in ones if i > r]

            # Split bottom by cols
            for c in range(n - 1):
                b1 = [(i, j) for (i, j) in bottom if j <= c]
                b2 = [(i, j) for (i, j) in bottom if j > c]
                best = min(best, rect_area(top) + rect_area(b1) + rect_area(b2))

            # Split top by cols
            for c in range(n - 1):
                t1 = [(i, j) for (i, j) in top if j <= c]
                t2 = [(i, j) for (i, j) in top if j > c]
                best = min(best, rect_area(bottom) + rect_area(t1) + rect_area(t2))

        # Case 4: Split as 1 vertical, then each half split horizontally
        for c in range(n - 1):
            left = [(i, j) for (i, j) in ones if j <= c]
            right = [(i, j) for (i, j) in ones if j > c]

            # Split left by rows
            for r in range(m - 1):
                l1 = [(i, j) for (i, j) in left if i <= r]
                l2 = [(i, j) for (i, j) in left if i > r]
                best = min(best, rect_area(right) + rect_area(l1) + rect_area(l2))

            # Split right by rows
            for r in range(m - 1):
                r1 = [(i, j) for (i, j) in right if i <= r]
                r2 = [(i, j) for (i, j) in right if i > r]
                best = min(best, rect_area(left) + rect_area(r1) + rect_area(r2))

        return best
