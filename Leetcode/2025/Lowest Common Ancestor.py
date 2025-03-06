# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return self.val


class Solution:

    def __init__(self):
        # Variable to store LCA node.
        self.ans = None

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def recurse_tree(current_node: TreeNode) -> bool:
            # If reached the end of a branch, return False.
            if not current_node:
                return False
            # Left Recursion
            left = recurse_tree(current_node.left)
            # Right Recursion
            right = recurse_tree(current_node.right)
            # If the current node is one of p or q
            mid = current_node.val == p or current_node.val == q
            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                self.ans = current_node.val
            # Return True if either of the three bool values is True.
            return mid or left or right
        # Traverse the tree
        recurse_tree(root)
        return self.ans

if __name__ == '__main__':
    node8 = TreeNode(8)
    node9 = TreeNode(9)
    node10 = TreeNode(10)
    node11 = TreeNode(11)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node4.left = node8
    node4.right = node9
    node5.left = node10
    node5.right = node11
    node2 = TreeNode(2)
    node2.left = node4
    node2.right = node5
    node1 = TreeNode(1)
    node3 = TreeNode(3)
    node1.left = node2
    node1.right = node3
    print(Solution().lowestCommonAncestor(node1, 9, 11))