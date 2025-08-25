from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        result = []
        diagonals = {}

        # Step 1: Group elements by diagonal (i + j)
        for i in range(m):
            for j in range(n):
                if i + j not in diagonals:
                    diagonals[i + j] = []
                diagonals[i + j].append(mat[i][j])

        # Step 2: Collect diagonals with direction handling
        for d in range(m + n - 1):
            if d % 2 == 0:
                # Reverse for even diagonals (up-right direction)
                result.extend(reversed(diagonals[d]))
            else:
                # Keep as is for odd diagonals (down-left direction)
                result.extend(diagonals[d])

        return result
