# Merge k sorted linked lists and return it as one sorted list.
#
# Example :
#
# 1 -> 10 -> 20
# 4 -> 11 -> 13
# 3 -> 8 -> 9
# will result in
#
# 1 -> 3 -> 4 -> 8 -> 9 -> 10 -> 11 -> 13 -> 20

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList:
    def __init__(self, x):
        self.val = x
        self.next = None

    def add(self, x):
        pass


class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        first_elements = dict([(index, value[0]) for index, value in enumerate(A)])
        pass


if __name__ == '__main__':
    s1 = Solution()

    s1.mergeKLists([])
