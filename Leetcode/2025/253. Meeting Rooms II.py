# https://leetcode.com/problems/meeting-rooms-ii/description/
import heapq
from typing import List

# O(n^2)
class Solution:
    # O(n^2)
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        rooms = [intervals[0]]
        for start_time, end_time in intervals[1:]:
            found = False
            for room_index, room_interval in enumerate(rooms):
                if start_time >= room_interval[1]:
                    found = True
                    rooms[room_index] = [start_time, end_time]
                    break
            if not found:
                rooms.append([start_time, end_time])
        return len(rooms)


class SolutionHeap:
    # O(n log n)
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        min_heap = [intervals[0][1]]
        for interval in intervals[1:]:
            min_end_time = min_heap[0]
            if interval[0] >= min_end_time:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval[1])
        return len(min_heap)

if __name__ == '__main__':
    print(Solution().minMeetingRooms([[0,30],[5,10],[15,20]]))
    print(Solution().minMeetingRooms([[7,10],[2,4]]))
    print(SolutionHeap().minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
    print(SolutionHeap().minMeetingRooms([[7, 10], [2, 4]]))