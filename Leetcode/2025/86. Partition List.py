# https://leetcode.com/problems/partition-list/description/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before_x_head = ListNode(-101)
        before = before_x_head
        after_x_head = ListNode(-101)
        after = after_x_head
        current = head
        while current:
            if current.val >= x:
                after.next = current
                current = current.next
                after = after.next
            else:
                before.next = current
                current = current.next
                before = before.next
        after.next = None
        before.next = after_x_head.next
        return before_x_head.next


if __name__ == '__main__':
    l = [1,4,3,2,5,2]
    _head = None
    _next = None
    for i in l[::-1]:
        ln = ListNode(i, _next)
        _next = ln
        _head = ln
    new_head = Solution().partition(_head, 3)
    while new_head:
        print(new_head.val)
        new_head = new_head.next