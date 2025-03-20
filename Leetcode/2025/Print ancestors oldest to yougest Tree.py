# Print ancestors from oldest to youngest in tree for given node

from copy import deepcopy


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def ancestors(self, root, target):
        answers = []
        def helper(curr_node, family):
            if curr_node is None:
                return
            if curr_node.val == target:
                answers.append(deepcopy(family + [curr_node.val]))
                return
            family.append(curr_node.val)
            helper(curr_node.left, family)
            helper(curr_node.right, family)
            family.pop()
        helper(root, [])
        return answers

if __name__ == '__main__':
    node7 = TreeNode(7)
    node4 = TreeNode(4)
    node2 = TreeNode(2, node7, node4)
    node6 = TreeNode(6)
    node5 = TreeNode(5, node6, node2)
    node0 = TreeNode(0)
    node8 = TreeNode(8)
    node1 = TreeNode(1, node0, node8)
    node3 = TreeNode(3, node5, node1)
    print(Solution().ancestors(node3, 4))
    print(Solution().ancestors(node3, 0))
    print(Solution().ancestors(node3, 1))
