class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        ans = 0
        
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + fruits[i][1]
        
        l = 0
        for r in range(n):
            # Move left pointer as long as the interval is not reachable
            while l <= r:
                left = fruits[l][0]
                right = fruits[r][0]
                cost1 = abs(startPos - left) + abs(right - left)
                cost2 = abs(startPos - right) + abs(right - left)
                if min(cost1, cost2) > k:
                    l += 1
                else:
                    break
            # Update answer if interval is valid
            if l <= r:
                total = prefix_sum[r+1] - prefix_sum[l]
                ans = max(ans, total)
        return ans
