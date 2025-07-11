import heapq
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        count = [0] * n
        free = list(range(n))
        heapq.heapify(free)  # Min-heap of free room indices
        busy = []  # Min-heap of (end_time, room_index)

        for start, end in meetings:
            # Free up rooms that are no longer busy
            while busy and busy[0][0] <= start:
                end_time, room = heapq.heappop(busy)
                heapq.heappush(free, room)

            if free:
                room = heapq.heappop(free)
                count[room] += 1
                heapq.heappush(busy, (end, room))
            else:
                end_time, room = heapq.heappop(busy)
                new_end = end_time + (end - start)
                count[room] += 1
                heapq.heappush(busy, (new_end, room))

        max_used = 0
        for i in range(n):
            if count[i] > count[max_used]:
                max_used = i

        return max_used
