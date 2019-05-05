# Definition for singly-linked list.
# https://leetcode.com/problems/add-two-numbers/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry_forward = 0
        p1 = l1
        p2 = l2
        result = ListNode(0)
        p3 = result
        while p1 or p2:
            temp_result = (p1.val if p1 else 0) + (p2.val if p1 else 0) + carry_forward
            to_be_used = temp_result % 10
            carry_forward = temp_result // 10
            p3.next = ListNode(to_be_used)
            p3 = p3.next
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next

        if carry_forward:
            p3.next = ListNode(carry_forward)

        return result.next



