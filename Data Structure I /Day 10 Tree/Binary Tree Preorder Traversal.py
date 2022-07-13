from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        queue = deque([root])
        preorder = []

        while queue:
            node = queue.pop()
            preorder.append(node.val)

            if node.right is not None:
                queue.append(node.right)
            if node.left is not None:
                queue.append(node.left)

        return preorder


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return list(self.preorder_generator(root))

    def preorder_generator(self, tree: Optional[TreeNode]):
        if tree is not None:
            yield tree.val
            yield from self.preorder_generator(tree.left)
            yield from self.preorder_generator(tree.right)
