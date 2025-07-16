
'''
3201. Find the Maximum Length of Valid Subsequence I

You are given an integer array nums.
A subsequence sub of nums with length x is called valid if it satisfies:

(sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2.
Return the length of the longest valid subsequence of nums.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: nums = [1,2,3,4]

Output: 4

Explanation:

The longest valid subsequence is [1, 2, 3, 4].

Example 2:

Input: nums = [1,2,1,1,2,1,2]

Output: 6

Explanation:

The longest valid subsequence is [1, 2, 1, 2, 1, 2].

Example 3:

Input: nums = [1,3]

Output: 2

Explanation:

The longest valid subsequence is [1, 3].

 

Constraints:

2 <= nums.length <= 2 * 105
1 <= nums[i] <= 107

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        

'''



class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # Count max alternating sequence (odd/even)
        def max_alternating():
            max_len = 1
            count = 1
            for i in range(1, len(nums)):
                if (nums[i] + nums[i - 1]) % 2 == (nums[i - 1] + nums[i - 2]) % 2 if i >= 2 else True:
                    count += 1
                else:
                    count = 2  # at least this pair is valid
                max_len = max(max_len, count)
            return max_len

        # Count number of even and odd elements
        odd = sum(1 for num in nums if num % 2 == 1)
        even = len(nums) - odd

        # Max length by only using same parity (even or odd)
        same_parity_len = max(odd, even)

        # Try alternating even-odd-even... (starting from even or odd)
        def max_alternating_parity(start_parity):
            count = 0
            expected = start_parity
            for num in nums:
                if num % 2 == expected:
                    count += 1
                    expected ^= 1  # flip between 0 and 1
            return count

        alt1 = max_alternating_parity(0)
        alt2 = max_alternating_parity(1)

        return max(same_parity_len, alt1, alt2)
