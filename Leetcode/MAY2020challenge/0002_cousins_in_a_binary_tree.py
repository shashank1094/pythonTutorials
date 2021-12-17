"""
https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3322/
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        global_var = {}

        def traversal(node, depth, parent_val):
            if node is None:
                return
            if node.val in [x, y]:
                global_var[node.val] = {
                    'parent': parent_val,
                    'depth': depth
                }
            traversal(node.left, depth + 1, node.val)
            traversal(node.right, depth + 1, node.val)

        traversal(root, 0, None)
        if global_var[x]['depth'] == global_var[y]['depth']:
            if global_var[x]['parent'] != global_var[y]['parent']:
                return True

        return False
