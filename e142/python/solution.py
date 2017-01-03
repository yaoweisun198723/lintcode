class Solution:
    """
    @param n: An integer
    @return: True or false
    """
    def checkPowerOf2(self, n):
        # write your code here
        if n < 1:
            return False
        if n == 1:
            return True
        while n > 1:
            if n % 2 == 1:
                return False
            n /= 2
        return True
        
