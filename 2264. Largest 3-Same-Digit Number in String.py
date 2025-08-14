class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ""
        for i in range(len(num) - 2):
            # check if 3 consecutive digits are the same
            if num[i] == num[i + 1] == num[i + 2]:
                candidate = num[i:i+3]
                # Update if this number is larger than the current answer
                if candidate > ans:
                    ans = candidate
        return ans
