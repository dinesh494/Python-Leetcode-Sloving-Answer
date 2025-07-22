class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        longest = ""
        for i in range(len(s)):
            # Odd length palindrome (centered at i)
            odd = expand_around_center(i, i)
            # Even length palindrome (centered between i and i+1)
            even = expand_around_center(i, i+1)

            # Update longest
            if len(odd) > len(longest):
                longest = odd
            if len(even) > len(longest):
                longest = even

        return longest
