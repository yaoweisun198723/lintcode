class Solution:
    """
    @param A : an integer array
    @return : a integer
    """
    def singleNumber(self, A):
        # write your code here
        res = 0
        for num in A:
            res = res ^ num;
        return res
