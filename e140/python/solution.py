class Solution:
    """
    @param a, b, n: 32bit integers
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        if n == 0:
            return 1 % b
        
        a = a % b
        """
        ans = 1
        while n>0:
            if n % 2 == 1:
                ans = (ans * a) % b
            n = n/2
            a = (a * a) % b 
        return ans
        """
        extra = 1
        while n > 0:
            if n % 2 == 1:
                extra *= a
            n = n / 2
            a = (a * a) % b
        return extra %b
