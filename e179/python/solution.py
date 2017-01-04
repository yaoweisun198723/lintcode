class Solution:
    #@param n, m: Two integer
    #@param i, j: Two bit positions
    #return: An integer
    def updateBits(self, n, m, i, j):
        # write your code here

        #tmp = n & (pow(2, j+1) - pow(2, i))
        tmp = n & ((1 << j+1) - (1 << i))
        #print tmp,n
        return self.int_overflow(n - tmp + (m << i))
        
    def int_overflow(self, val):
        maxint = 2147483647  
        if not -maxint-1 <= val <= maxint:  
            val = (val + (maxint + 1)) % (2 * (maxint + 1)) - maxint - 1  
        return val 
