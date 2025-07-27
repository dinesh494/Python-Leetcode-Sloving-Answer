class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        # Step 1: Remove consecutive duplicates
        filtered = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                filtered.append(nums[i])
        
        count = 0
        # Step 2: Check each number (except the first and last)
        for i in range(1, len(filtered) - 1):
            if filtered[i] > filtered[i - 1] and filtered[i] > filtered[i + 1]:
                count += 1  # hill
            elif filtered[i] < filtered[i - 1] and filtered[i] < filtered[i + 1]:
                count += 1  # valley
                
        return count
