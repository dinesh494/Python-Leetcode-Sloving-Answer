class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mx = max(nums)
        max_len = 0
        cur_len = 0

        for n in nums:
            if n == mx:
                cur_len += 1
                max_len = max(max_len, cur_len)
            else:
                cur_len = 0
        return max_len
