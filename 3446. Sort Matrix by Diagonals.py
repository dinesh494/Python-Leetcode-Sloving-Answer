from collections import defaultdict

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        diagonals = defaultdict(list)

        # Group elements by diagonal
        for i in range(n):
            for j in range(n):
                diagonals[i - j].append(grid[i][j])
        
        # Sort each diagonal
        for k in diagonals:
            if k >= 0:
                diagonals[k].sort(reverse=True)
            else:
                diagonals[k].sort()
        
        # Reconstruct the matrix
        result = [[0] * n for _ in range(n)]
        indices = defaultdict(int)

        for i in range(n):
            for j in range(n):
                k = i - j
                result[i][j] = diagonals[k][indices[k]]
                indices[k] += 1
        
        return result
