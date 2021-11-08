# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/
# Definition for singly-linked list.
import sys
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        r = self.next.val if self.next else ' '
        return f'{self.val} -> {r}'


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        n = 0
        curr_node = head
        while curr_node:
            curr_node = curr_node.next
            n += 1
        ans = [-1, -1]
        critical_indexes = []
        if n < 4:
            return ans
        prev_node = head
        curr_node = head.next
        next_node = head.next.next
        count = 1
        while next_node:
            if curr_node.val > prev_node.val and curr_node.val > next_node.val:
                critical_indexes.append(count)
            if curr_node.val < prev_node.val and curr_node.val < next_node.val:
                critical_indexes.append(count)
            count += 1
            prev_node = curr_node
            curr_node = next_node
            next_node = next_node.next

        # import pprint
        # pprint.pprint(critical_indexes)

        _min = sys.maxsize
        if len(critical_indexes) < 2:
            return ans
        for i in range(1, len(critical_indexes)):
            curr_diff = critical_indexes[i] - critical_indexes[i-1]
            if curr_diff < _min:
                _min = curr_diff
        _max = critical_indexes[-1] - critical_indexes[0]
        ans = [_min, _max]
        return ans


if __name__ == '__main__':
    arr = [2, 3, 3, 2]
    arr.reverse()
    prev = None
    for elem in arr:
        t = ListNode(elem, prev)
        prev = t
    prev
    print(Solution().nodesBetweenCriticalPoints(prev))
