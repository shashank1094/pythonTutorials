# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.count = 0
        if not root:
            return 0
        has_cam, is_covered = self.util(root)
        print(has_cam, is_covered)
        if not has_cam and not is_covered:
            self.count += 1
        return self.count if self.count else 1

    def util(self, root):
        if not root:
            return False, True

        left_cam, from_left = self.util(root.left)
        right_cam, from_right = self.util(root.right)
        is_covered = left_cam or right_cam
        should_have_cam = (not (from_left and from_right))
        if should_have_cam:
            self.count += 1
        # print(should_have_cam, is_covered or should_have_cam)
        return should_have_cam, is_covered or should_have_cam
