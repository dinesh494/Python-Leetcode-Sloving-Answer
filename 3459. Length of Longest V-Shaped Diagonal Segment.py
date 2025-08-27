import collections
from typing import List

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        # DP tables: dp[(type, dir)][i][j]
        # type: 0, 1, 2 (for sequences starting with 0, 1, 2)
        # dir: 0:in_tl, 1:in_tr, 2:in_bl, 3:in_br
        #      4:out_br, 5:out_bl, 6:out_tr, 7:out_tl
        dp = collections.defaultdict(lambda: [[0] * m for _ in range(n)])

        # --- Calculate IN-going DP tables ---
        
        # Dir 0: IN from TL (prev: i-1, j-1)
        for i in range(n):
            for j in range(m):
                # type 1
                if grid[i][j] == 1: dp[1, 0][i][j] = 1
                elif i > 0 and j > 0 and dp[1, 0][i-1][j-1] > 0:
                    prev_len = dp[1, 0][i-1][j-1]
                    if grid[i][j] == (2 if prev_len % 2 != 0 else 0): dp[1, 0][i][j] = prev_len + 1
                # type 2
                if grid[i][j] == 2: dp[2, 0][i][j] = 1
                elif i > 0 and j > 0 and dp[2, 0][i-1][j-1] > 0:
                    prev_len = dp[2, 0][i-1][j-1]
                    if grid[i][j] == (0 if prev_len % 2 != 0 else 2): dp[2, 0][i][j] = prev_len + 1
                # type 0
                if grid[i][j] == 0: dp[0, 0][i][j] = 1
                elif i > 0 and j > 0 and dp[0, 0][i-1][j-1] > 0:
                    prev_len = dp[0, 0][i-1][j-1]
                    if grid[i][j] == (2 if prev_len % 2 != 0 else 0): dp[0, 0][i][j] = prev_len + 1

        # Dir 1: IN from TR (prev: i-1, j+1)
        for i in range(n):
            for j in range(m - 1, -1, -1):
                if grid[i][j] == 1: dp[1, 1][i][j] = 1
                elif i > 0 and j < m - 1 and dp[1, 1][i-1][j+1] > 0:
                    prev_len = dp[1, 1][i-1][j+1]
                    if grid[i][j] == (2 if prev_len % 2 != 0 else 0): dp[1, 1][i][j] = prev_len + 1
                if grid[i][j] == 2: dp[2, 1][i][j] = 1
                elif i > 0 and j < m - 1 and dp[2, 1][i-1][j+1] > 0:
                    prev_len = dp[2, 1][i-1][j+1]
                    if grid[i][j] == (0 if prev_len % 2 != 0 else 2): dp[2, 1][i][j] = prev_len + 1
                if grid[i][j] == 0: dp[0, 1][i][j] = 1
                elif i > 0 and j < m - 1 and dp[0, 1][i-1][j+1] > 0:
                    prev_len = dp[0, 1][i-1][j+1]
                    if grid[i][j] == (2 if prev_len % 2 != 0 else 0): dp[0, 1][i][j] = prev_len + 1

        # Dir 2: IN from BL (prev: i+1, j-1)
        for i in range(n - 1, -1, -1):
            for j in range(m):
                if grid[i][j] == 1: dp[1, 2][i][j] = 1
                elif i < n - 1 and j > 0 and dp[1, 2][i+1][j-1] > 0:
                    prev_len = dp[1, 2][i+1][j-1]
                    if grid[i][j] == (2 if prev_len % 2 != 0 else 0): dp[1, 2][i][j] = prev_len + 1
                if grid[i][j] == 2: dp[2, 2][i][j] = 1
                elif i < n - 1 and j > 0 and dp[2, 2][i+1][j-1] > 0:
                    prev_len = dp[2, 2][i+1][j-1]
                    if grid[i][j] == (0 if prev_len % 2 != 0 else 2): dp[2, 2][i][j] = prev_len + 1
                if grid[i][j] == 0: dp[0, 2][i][j] = 1
                elif i < n - 1 and j > 0 and dp[0, 2][i+1][j-1] > 0:
                    prev_len = dp[0, 2][i+1][j-1]
                    if grid[i][j] == (2 if prev_len % 2 != 0 else 0): dp[0, 2][i][j] = prev_len + 1

        # Dir 3: IN from BR (prev: i+1, j+1)
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if grid[i][j] == 1: dp[1, 3][i][j] = 1
                elif i < n - 1 and j < m - 1 and dp[1, 3][i+1][j+1] > 0:
                    prev_len = dp[1, 3][i+1][j+1]
                    if grid[i][j] == (2 if prev_len % 2 != 0 else 0): dp[1, 3][i][j] = prev_len + 1
                if grid[i][j] == 2: dp[2, 3][i][j] = 1
                elif i < n - 1 and j < m - 1 and dp[2, 3][i+1][j+1] > 0:
                    prev_len = dp[2, 3][i+1][j+1]
                    if grid[i][j] == (0 if prev_len % 2 != 0 else 2): dp[2, 3][i][j] = prev_len + 1
                if grid[i][j] == 0: dp[0, 3][i][j] = 1
                elif i < n - 1 and j < m - 1 and dp[0, 3][i+1][j+1] > 0:
                    prev_len = dp[0, 3][i+1][j+1]
                    if grid[i][j] == (2 if prev_len % 2 != 0 else 0): dp[0, 3][i][j] = prev_len + 1

        # --- Calculate OUT-going DP tables ---
        
        # Dir 4: OUT to BR (next: i+1, j+1)
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                ni, nj = i + 1, j + 1
                if grid[i][j] == 2: dp[2, 4][i][j] = 1 + (dp[0, 4][ni][nj] if ni < n and nj < m else 0)
                if grid[i][j] == 0: dp[0, 4][i][j] = 1 + (dp[2, 4][ni][nj] if ni < n and nj < m else 0)
        
        # Dir 5: OUT to BL (next: i+1, j-1)
        for i in range(n - 1, -1, -1):
            for j in range(m):
                ni, nj = i + 1, j - 1
                if grid[i][j] == 2: dp[2, 5][i][j] = 1 + (dp[0, 5][ni][nj] if ni < n and nj >= 0 else 0)
                if grid[i][j] == 0: dp[0, 5][i][j] = 1 + (dp[2, 5][ni][nj] if ni < n and nj >= 0 else 0)
                
        # Dir 6: OUT to TR (next: i-1, j+1)
        for i in range(n):
            for j in range(m - 1, -1, -1):
                ni, nj = i - 1, j + 1
                if grid[i][j] == 2: dp[2, 6][i][j] = 1 + (dp[0, 6][ni][nj] if ni >= 0 and nj < m else 0)
                if grid[i][j] == 0: dp[0, 6][i][j] = 1 + (dp[2, 6][ni][nj] if ni >= 0 and nj < m else 0)

        # Dir 7: OUT to TL (next: i-1, j-1)
        for i in range(n):
            for j in range(m):
                ni, nj = i - 1, j - 1
                if grid[i][j] == 2: dp[2, 7][i][j] = 1 + (dp[0, 7][ni][nj] if ni >= 0 and nj >= 0 else 0)
                if grid[i][j] == 0: dp[0, 7][i][j] = 1 + (dp[2, 7][ni][nj] if ni >= 0 and nj >= 0 else 0)

        # --- Combine and find max length ---
        max_len = 0
        for i in range(n):
            for j in range(m):
                for d in range(4): # Straight lines
                    max_len = max(max_len, dp[1, d][i][j])
                
                # Turns
                # In from TL (0) -> Out to BL (5)
                l1 = dp[1, 0][i][j]
                if l1 > 0:
                    ni, nj = i + 1, j - 1
                    if 0 <= ni < n and 0 <= nj < m:
                        l2 = dp[2, 5][ni][nj] if l1 % 2 != 0 else dp[0, 5][ni][nj]
                        if l2 > 0: max_len = max(max_len, l1 + l2)
                
                # In from TR (1) -> Out to TL (7)
                l1 = dp[1, 1][i][j]
                if l1 > 0:
                    ni, nj = i - 1, j - 1
                    if 0 <= ni < n and 0 <= nj < m:
                        l2 = dp[2, 7][ni][nj] if l1 % 2 != 0 else dp[0, 7][ni][nj]
                        if l2 > 0: max_len = max(max_len, l1 + l2)

                # In from BR (3) -> Out to TR (6)
                l1 = dp[1, 3][i][j]
                if l1 > 0:
                    ni, nj = i - 1, j + 1
                    if 0 <= ni < n and 0 <= nj < m:
                        l2 = dp[2, 6][ni][nj] if l1 % 2 != 0 else dp[0, 6][ni][nj]
                        if l2 > 0: max_len = max(max_len, l1 + l2)

                # In from BL (2) -> Out to BR (4)
                l1 = dp[1, 2][i][j]
                if l1 > 0:
                    ni, nj = i + 1, j + 1
                    if 0 <= ni < n and 0 <= nj < m:
                        l2 = dp[2, 4][ni][nj] if l1 % 2 != 0 else dp[0, 4][ni][nj]
                        if l2 > 0: max_len = max(max_len, l1 + l2)
                        
        return max_len
