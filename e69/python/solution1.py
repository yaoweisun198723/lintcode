Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of binary tree.
    @return: Level order in a list of lists of integers
    """
    def levelOrder(self, root):
        # write your code here
        order_list = []
        self.recursiveLevel(root, 0, order_list)
        return order_list
        
    def recursiveLevel(self, root, level, order_list):
        if root is None:
            return
        if len(order_list) < level + 1:
            order_list.append([])
        order_list[level].append(root.val)
        self.recursiveLevel(root.left, level+1, order_list)
        self.recursiveLevel(root.right, level+1, order_list)
