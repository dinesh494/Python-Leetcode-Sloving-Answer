class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diagonal_squared = 0
        max_area = 0

        for length, width in dimensions:
            diagonal_squared = length * length + width * width
            area = length * width

            if diagonal_squared > max_diagonal_squared:
                max_diagonal_squared = diagonal_squared
                max_area = area
            elif diagonal_squared == max_diagonal_squared:
                max_area = max(max_area, area)
        
        return max_area
