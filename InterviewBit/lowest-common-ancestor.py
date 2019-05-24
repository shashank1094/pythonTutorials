# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def lca(self, A, B, C):
        self.B = B
        self.C = C
        self.ans = None
        self.pre_order(A)

        return self.ans if self.ans else -1


    def pre_order(self, root):
        if not root:
            return False

        left = self.pre_order(root.left)
        right = self.pre_order(root.right)

        if root.val == self.B and root.val == self.C and not self.ans:
            self.ans = root.val

        if left and right and not self.ans:
            self.ans = root.val

        if (left or right) and (root.val == self.B or root.val == self.C) and not self.ans:
            self.ans = root.val

        return left or right or (root.val == self.B or root.val == self.C)

