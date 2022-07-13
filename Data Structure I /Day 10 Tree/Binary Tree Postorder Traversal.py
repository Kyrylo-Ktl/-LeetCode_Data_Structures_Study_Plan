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

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        postorder = []
        stack = [root]

        while stack:
            node = stack.pop()
            postorder.append(node.val)
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)

        return postorder[::-1]


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return list(self.postorder_generator(root))

    def postorder_generator(self, tree: Optional[TreeNode]):
        if tree is not None:
            yield from self.postorder_generator(tree.left)
            yield from self.postorder_generator(tree.right)
            yield tree.val
