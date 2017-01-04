class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """ 
    def uniquePaths(self, m, n):
        # write your code here
        ret = 1
        for i in range(n, m+n-1):
            ret *= i
        for j in range(1, m):
            ret /= j
        return ret
