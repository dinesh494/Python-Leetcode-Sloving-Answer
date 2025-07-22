class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            # Shrink the window until s[right] is not in the set
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # Add current character and update max length
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length
