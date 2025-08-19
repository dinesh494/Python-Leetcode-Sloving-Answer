class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0   # running total of subarrays
        zeros = 0   # current consecutive zero run length

        for num in nums:
            if num == 0:
                zeros += 1         # extend current zero run
                count += zeros     # add subarrays ending here
            else:
                zeros = 0          # reset for non-zero
        
        return count
