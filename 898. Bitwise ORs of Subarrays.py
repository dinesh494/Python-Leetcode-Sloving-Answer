class Solution:
    def subarrayBitwiseORs(self, arr):
        res_set = set()
        prev_set = set()
        for num in arr:
            curr_set = {num}
            for prev in prev_set:
                curr_set.add(prev | num)
            res_set |= curr_set
            prev_set = curr_set
        return len(res_set)
