from collections import Counter

class Solution:
    def minCost(self, basket1: list[int], basket2: list[int]) -> int:
        # Frequency count of fruits in both baskets combined
        count = Counter(basket1) + Counter(basket2)

        # Check for odd counts, if any fruit count is odd, return -1
        for v in count.values():
            if v % 2 != 0:
                return -1

        # Frequency count for each basket separately
        count1 = Counter(basket1)
        count2 = Counter(basket2)

        # Minimum fruit cost from both baskets
        min_fruit_cost = min(min(basket1), min(basket2))

        # List of fruits to swap out from basket1 and basket2
        swap1 = []
        swap2 = []

        # Calculate which fruits are in excess in one basket compared to the other
        for fruit in count:
            diff = count1[fruit] - count2[fruit]
            if diff > 0:
                swap1.extend([fruit] * (diff // 2))
            elif diff < 0:
                swap2.extend([fruit] * (-diff // 2))

        # Sort the swap lists to minimize cost by pairing smallest and largest
        swap1.sort()
        swap2.sort(reverse=True)

        total_cost = 0
        for f1, f2 in zip(swap1, swap2):
            # Either swap directly or use double swap with smallest fruit as intermediary
            cost = min(min(f1, f2), 2 * min_fruit_cost)
            total_cost += cost

        return total_cost
