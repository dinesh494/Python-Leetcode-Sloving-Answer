class Solution:
    def maxCollectedFruits(self, fruits):
        n = len(fruits)
        total = 0

        # Collect main diagonal fruits (child 1)
        for i in range(n):
            total += fruits[i][i]

        rightPath = [0] * 3
        rightPath[0] = fruits[0][n - 1]

        bottomPath = [0] * 3
        bottomPath[0] = fruits[n - 1][0]

        window = 2

        for step in range(1, n - 1):
            newRight = [0] * (window + 2)
            newBottom = [0] * (window + 2)

            for dist in range(window):
                # For rightPath (child 2)
                left = rightPath[dist - 1] if dist - 1 >= 0 else 0
                mid = rightPath[dist]
                right = rightPath[dist + 1] if dist + 1 < len(rightPath) else 0
                col = n - 1 - dist
                if 0 <= step < n and 0 <= col < n:
                    newRight[dist] = max(left, mid, right) + fruits[step][col]

                # For bottomPath (child 3)
                left = bottomPath[dist - 1] if dist - 1 >= 0 else 0
                mid = bottomPath[dist]
                right = bottomPath[dist + 1] if dist + 1 < len(bottomPath) else 0
                row = n - 1 - dist
                if 0 <= row < n and 0 <= step < n:
                    newBottom[dist] = max(left, mid, right) + fruits[row][step]

            rightPath = newRight
            bottomPath = newBottom

            if window - n + 4 + step <= 1:
                window += 1
            elif window - n + 3 + step > 1:
                window -= 1

        return total + rightPath[0] + bottomPath[0]
