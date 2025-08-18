from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def dfs(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6  # Allow for floating point errors

            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        # Pick numbers at i and j
                        next_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]
                        # Try all possible computations between nums[i] and nums[j]
                        for op in ['+', '-', '*', '/']:
                            if op == '+':
                                new_num = nums[i] + nums[j]
                            elif op == '-':
                                new_num = nums[i] - nums[j]
                            elif op == '*':
                                new_num = nums[i] * nums[j]
                            elif op == '/':
                                if nums[j] == 0:
                                    continue
                                new_num = nums[i] / nums[j]
                            if dfs(next_nums + [new_num]):
                                return True
            return False

        return dfs([float(x) for x in cards])
