class Solution:
    def myAtoi(self, s: str) -> int:
        i, n, sign, result = 0, len(s), 1, 0

        # Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1
        # Handle sign
        if i < n and (s[i] == '-' or s[i] == '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        # Build number and check for overflows
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            if result > (2**31 - 1) // 10 or (result == (2**31 - 1) // 10 and digit > 7):
                return 2**31 - 1 if sign == 1 else -2**31
            result = result * 10 + digit
            i += 1
        return sign * result
