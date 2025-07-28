"""
        1
    2       2
  3   4  4     3
"""


class Node:
    def __init__(self, val, _left=None, _right=None):
        self.value = val
        self.left = _left
        self.right = _right


class Tree:
    def __init__(self, _node=None):
        self.root = _node


def helper(node1, node2):
    if node1 is None and node2 is None:
        return True
    elif node1 is not None and node2 is not None:
        return node1.value == node2.value and helper(node1.left, node2.right) and helper(node1.right, node2.left)
    else:
        return False


def is_symmetric(tree):
    root = tree.root
    if not root:
        return
    return helper(root.left, root.right)


if __name__ == '__main__':
    n3_1 = Node(3)
    n4_1 = Node(4)
    n2_1 = Node(2, n3_1, n4_1)

    n3_2 = Node(3)
    n4_2 = Node(5)
    n2_2 = Node(2, n4_2, n3_2)

    n1 = Node(1, n2_1, n2_2)
    t = Tree(n1)
    print(is_symmetric(t))
