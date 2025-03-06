# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        pass
if __name__ == '__main__':
    t5 = TreeNode(5)
    t1 = TreeNode(1)
    t3 = TreeNode(3)
    t3.left = t5
    t3.right = t1



    print(Solution().distanceK(t1, t5, 2))