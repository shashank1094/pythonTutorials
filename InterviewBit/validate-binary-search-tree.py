# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBSTutil(self, root, range_low, range_high):
        if not root:
            return True
        if range_low is not None:
            if root.val <= range_low:
                return False
        if range_high is not None:
            if root.val >= range_high:
                return False
        return self.isValidBSTutil(root.left, range_low, root.val) and self.isValidBSTutil(root.right, root.val,
                                                                                           range_high)
