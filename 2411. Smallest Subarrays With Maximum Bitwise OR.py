class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        last = [0] * 32  # stores the last index seen of each bit (0-31)

        for i in range(n - 1, -1, -1):
            # update 'last' for set bits in nums[i]
            for bit in range(32):
                if nums[i] & (1 << bit):
                    last[bit] = i
            # to get max OR, need to include till the farthest index with any bit set
            farthest = i
            for bit in range(32):
                farthest = max(farthest, last[bit])
            ans[i] = farthest - i + 1

        return ans
