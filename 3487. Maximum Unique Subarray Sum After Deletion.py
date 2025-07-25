class Solution:
    def maxSum(self, nums: List[int]) -> int:
        # Find the maximum value in the array
        max_val = max(nums)

        # If the maximum value is less than or equal to 0, return it
        if max_val <= 0:
            return max_val

        # Boolean array to keep track of numbers that have been added (range: -100 to 100 → size = 201)
        seen = [False] * 201  # Index 0 corresponds to -100, index 200 to 100
        result = 0

        for num in nums:
            # Skip negative numbers or already seen numbers
            if num < 0 or seen[num + 100]:  # shift index to positive
                continue

            # Add to result and mark as seen
            result += num
            seen[num + 100] = True

        return result
