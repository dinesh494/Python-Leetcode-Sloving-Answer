from typing import List

class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        valid_subarrays = 0
        max_left = 0
        second_max_left = 0
        gains = [0] * (n + 1)
        conflicts = [[] for _ in range(n + 1)]

        for a, b in conflictingPairs:
            conflicts[max(a, b)].append(min(a, b))

        for right in range(1, n + 1):
            for left in conflicts[right]:
                if left > max_left:
                    second_max_left = max_left
                    max_left = left
                elif left > second_max_left:
                    second_max_left = left
            # Subarrays [max_left + 1..right], ..., [right..right] are valid.
            valid_subarrays += right - max_left
            # If we remove `max_left`, we can gain these new subarrays:
            gains[max_left] += max_left - second_max_left

        return valid_subarrays + max(gains)
