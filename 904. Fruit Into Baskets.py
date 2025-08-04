from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        from collections import defaultdict

        # Dictionary to count each fruit in the current window
        count = defaultdict(int)
        left = 0
        max_fruits = 0

        for right in range(len(fruits)):
            # Add the current fruit to the count
            count[fruits[right]] += 1
            
            # If we have more than 2 types of fruits in baskets, move left pointer
            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1
            
            # Update the maximum window size
            max_fruits = max(max_fruits, right - left + 1)
        
        return max_fruits
