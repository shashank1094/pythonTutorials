# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        l = self.left.val if self.left else ' '
        r = self.right.val if self.right else ' '
        return f' {l} <-{self.val} -> {r} '

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        total = 0

        def helper(curr_node, curr_num):
            if curr_node is None:
                return
            if curr_node is not None and curr_node.left is None and curr_node.right is None:
                nonlocal total
                total += curr_node.val + (curr_num * 10)
                return
            curr_num = (curr_num * 10) + curr_node.val
            helper(curr_node.left, curr_num)
            helper(curr_node.right, curr_num)

        helper(root, 0)
        return total


if __name__ == '__main__':
    # tree_node5 = TreeNode(5)
    # tree_node1 = TreeNode(1)
    # tree_node9 = TreeNode(9, tree_node5, tree_node1)
    # tree_node0 = TreeNode(0)
    #
    # tree_node4 = TreeNode(4, tree_node9, tree_node0)
    #
    # print(Solution().sumNumbers(tree_node4))


    tree_node1 = TreeNode(1)
    tree_node0 = TreeNode(0, tree_node1)

    print(Solution().sumNumbers(tree_node0))
