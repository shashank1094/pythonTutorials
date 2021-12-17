# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        self.ans = {}
        self.util(root, 0, 0)
        x_sorted = sorted(list(self.ans.values()), key=lambda x: x['priority'])
        print(x_sorted)
        x_sorted = [x['nodes'] for x in x_sorted]

        f = []
        for entry in x_sorted:
            s = sorted(entry, key=lambda x: (-1 * x['p'], x['val']))
            f.append([x['val'] for x in s])

        return f

    def util(self, root, x, y):
        if root is None:
            return
        if self.ans.get(x) is None:
            self.ans[x] = {"priority": x, "nodes": []}
        self.ans[x]["nodes"].append({"val": root.val, "p": y})
        self.util(root.left, x - 1, y - 1)
        self.util(root.right, x + 1, y - 1)
