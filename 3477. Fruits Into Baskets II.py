class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        # Track which baskets are occupied
        used = [False] * n
        unplaced = 0

        for fruit_qty in fruits:
            placed = False
            for i in range(n):
                if not used[i] and baskets[i] >= fruit_qty:
                    used[i] = True
                    placed = True
                    break
            if not placed:
                unplaced += 1

        return unplaced
