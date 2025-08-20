from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        total = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1   # first row/col → only 1x1 square possible
                    else:
                        dp[i][j] = min(
                            dp[i-1][j],      # top
                            dp[i][j-1],      # left
                            dp[i-1][j-1]     # top-left
                        ) + 1
                    total += dp[i][j]
        return total
