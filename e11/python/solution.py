"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of the binary search tree.
    @param k1 and k2: range k1 to k2.
    @return: Return all keys that k1<=key<=k2 in ascending order.
    """     
    def searchRange(self, root, k1, k2):
        # write your code here
        result = []
        self.reverse(result, root, k1, k2)
        return result
    
    def reverse(self, result, root, k1, k2):    
        if k1 <= k2 and root != None:
            val = root.val
            self.reverse(result, root.left, k1, min(k2, val))
            if k1 <= val <= k2:
                result.append(val)
            self.reverse(result, root.right, max(k1, val), k2)
        
