class Solution(object):
    def soupServings(self, n):
        if n > 5000:
            return 1.0
        n = (n + 24) // 25
        memo = {}
        def dp(a, b):
            if (a, b) in memo:
                return memo[(a, b)]
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
            memo[(a, b)] = 0.25 * (
                dp(a-4, b) +
                dp(a-3, b-1) +
                dp(a-2, b-2) +
                dp(a-1, b-3)
            )
            return memo[(a, b)]
        return dp(n, n)
