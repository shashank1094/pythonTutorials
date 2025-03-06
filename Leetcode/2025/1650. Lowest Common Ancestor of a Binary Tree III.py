# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/description/
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor_withoutParentPointer(self, root ,p , q):
        lca = None
        def dfs(curr_node):
            nonlocal lca
            if not curr_node:
                return False
            is_left = dfs(curr_node.left)
            is_right = dfs(curr_node.right)
            is_curr = curr_node.val in [q, p]
            if (is_left and is_right) or ((is_left or is_right) and is_curr):
                lca = curr_node.val
            return is_left or is_right or is_curr
        dfs(root)
        return lca

    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        visited_map = {}
        lca = None
        queue_p = deque([p])
        queue_q = deque([q])
        while len(queue_p) or len(queue_q):
            if len(queue_p):
                curr_p = queue_p.pop()
                if curr_p.val in visited_map:
                    lca = curr_p
                    break
                visited_map[curr_p.val] = visited_map
                if curr_p.parent:
                    queue_p.appendleft(curr_p.parent)
            if len(queue_q):
                curr_q = queue_q.pop()
                if curr_q.val in visited_map:
                    lca = curr_q
                    break
                visited_map[curr_q.val] = visited_map
                if curr_q.parent:
                    queue_q.appendleft(curr_q.parent)
        return lca

if __name__ == '__main__':
    node7 = Node(7)
    node4 = Node(4)
    node2 = Node(2)
    node2.left = node7
    node2.right = node4
    node7.parent = node2
    node4.parent = node2
    node6 = Node(6)
    node5 = Node(5)
    node5.left = node6
    node5.right = node2
    node6.parent = node5
    node2.parent = node5
    node0 = Node(0)
    node8 = Node(8)
    node1 = Node(1)
    node1.left = node0
    node1.right = node8
    node0.parent = node1
    node8.parent = node1
    node3 = Node(3)
    node3.left = node5
    node3.right = node1
    node5.parent = node3
    node1.parent = node3
    print(Solution().lowestCommonAncestor_withoutParentPointer(node3, 6,4))
    print(Solution().lowestCommonAncestor_withoutParentPointer(node3, 3, 7))
    print(Solution().lowestCommonAncestor(node6, node4).val)
    print(Solution().lowestCommonAncestor(node3, node7).val)
