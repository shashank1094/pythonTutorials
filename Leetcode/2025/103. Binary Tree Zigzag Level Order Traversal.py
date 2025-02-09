# Definition for a binary tree node.
import copy


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [(root, 0)]
        answer = []
        current_list = []
        prev_depth = 0
        while len(queue):
            current_node, current_depth = queue.pop(0)
            if prev_depth != current_depth:
                answer.append(copy.deepcopy(current_list))
                current_list = []
                prev_depth = current_depth
            if current_node is None:
                continue
            if current_depth % 2:
                current_list.insert(0, current_node.val)
            else:
                current_list.append(current_node.val)
            queue.append((current_node.left, current_depth+1))
            queue.append((current_node.right, current_depth + 1))
        return answer



if __name__ == '__main__':
    tn2 = TreeNode(2, None, None)
    tn3 = TreeNode(3, None, None)
    tn1 = TreeNode(1, tn2, tn3)
    print(Solution().zigzagLevelOrder(tn1))