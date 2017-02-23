"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: Inorder in ArrayList which contains node values.
    """
    # morris traversal
    def inorderTraversal(self, root):
        result = []
        current = root
        while current:
            if not current.left:
                result.append(current.val)
                current = current.right
            else:
                most_right = self.findRight(current)
                if most_right.right == current:
                    result.append(current.val)
                    current = current.right
                    most_right.right = None
                else:
                    most_right.right = current
                    current = current.left

        return result
        
    def findRight(self, root):
        p = root.left
        if not p:
            return None
        while p.right and p.right != root:
            p = p.right
        return p
