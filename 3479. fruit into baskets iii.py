class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.build(nums, 0, 0, self.n - 1)

    def build(self, nums, idx, l, r):
        if l == r:
            self.tree[idx] = nums[l]
            return
        m = (l + r) // 2
        self.build(nums, idx * 2 + 1, l, m)
        self.build(nums, idx * 2 + 2, m + 1, r)
        self.tree[idx] = max(self.tree[idx * 2 + 1], self.tree[idx * 2 + 2])

    def update(self, i, val, idx=0, l=0, r=None):
        if r is None: r = self.n - 1
        if l == r:
            self.tree[idx] = val
            return
        m = (l + r) // 2
        if i <= m:
            self.update(i, val, idx * 2 + 1, l, m)
        else:
            self.update(i, val, idx * 2 + 2, m + 1, r)
        self.tree[idx] = max(self.tree[idx * 2 + 1], self.tree[idx * 2 + 2])

    def query_first(self, target, idx=0, l=0, r=None):
        if r is None: r = self.n - 1
        if self.tree[idx] < target:
            return -1
        if l == r:
            return l
        m = (l + r) // 2
        res = self.query_first(target, idx * 2 + 1, l, m)
        if res != -1: return res
        return self.query_first(target, idx * 2 + 2, m + 1, r)

class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        n = len(fruits)
        seg = SegmentTree(baskets)
        unplaced = 0

        for fruit in fruits:
            idx = seg.query_first(fruit)
            if idx == -1:
                unplaced += 1
            else:
                seg.update(idx, -1)  # Mark this basket as used
        return unplaced
