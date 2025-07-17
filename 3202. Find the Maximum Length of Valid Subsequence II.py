
'''
3202. Find the Maximum Length of Valid Subsequence II

You are given an integer array nums and a positive integer k.
A subsequence sub of nums with length x is called valid if it satisfies:

(sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k.
Return the length of the longest valid subsequence of nums.
 

Example 1:

Input: nums = [1,2,3,4,5], k = 2

Output: 5

Explanation:

The longest valid subsequence is [1, 2, 3, 4, 5].

Example 2:

Input: nums = [1,4,2,3,1,4], k = 3

Output: 4

Explanation:

The longest valid subsequence is [1, 4, 1, 4].

 

Constraints:

2 <= nums.length <= 103
1 <= nums[i] <= 107
1 <= k <= 103
'''


class Solution:
    def maximumLength(self, nums, k):
        n = len(nums)
        from collections import defaultdict

        dp = [defaultdict(int) for _ in range(n)]
        max_len = 1

        for i in range(n):
            for j in range(i):
                mod = (nums[i] + nums[j]) % k
                dp[i][mod] = max(dp[i][mod], dp[j][mod] + 1 if mod in dp[j] else 2)
                max_len = max(max_len, dp[i][mod])

        return max_len
