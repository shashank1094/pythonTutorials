# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return 'None'
        data = []
        def preorder(node):
            if not node:
                data.append('None')
                return
            data.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return ','.join(data)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == 'None':
            return
        def helper(data_list):
            if data_list[0] == 'None':
                data_list.pop(0)
                return None
            val = data_list.pop(0)
            node = TreeNode(val)
            node.left = helper(data_list)
            node.right = helper(data_list)
            return node
        return helper(data.split(','))


if __name__ == '__main__':
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t3 = TreeNode(3, t4, t5)
    t2 = TreeNode(2)
    root = TreeNode(1, t2, t3)
    # Your Codec object will be instantiated and called as such:
    ser = Codec()
    deser = Codec()
    print(ser.serialize(root))
    re_root = deser.deserialize(ser.serialize(root))
    def pre_order(node):
        if not node:
            return
        print(node.val, end= ' ')
        pre_order(node.left)
        pre_order(node.right)
    pre_order(root)
    print("")
    pre_order(re_root)
