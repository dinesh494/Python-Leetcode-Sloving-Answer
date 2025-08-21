from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        count = 0
        heights = [0] * n   # continuous ones height for each column

        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    heights[col] = 0
                else:
                    heights[col] += 1

            # now count submatrices using stack
            stack = []
            sum_submat = [0] * n
            for i in range(n):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                
                if stack:
                    prev_index = stack[-1]
                    sum_submat[i] = sum_submat[prev_index] + heights[i] * (i - prev_index)
                else:
                    sum_submat[i] = heights[i] * (i + 1)
                
                stack.append(i)

            count += sum(sum_submat)

        return count
