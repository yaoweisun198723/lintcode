class Solution:
    """
    @param a, b: Two integer
    return: An integer
    """
    #ref:http://blog.csdn.net/guoziqing506/article/details/51601472
    def bitSwapRequired(self, a, b):
        # write your code here
        a ^= b
        if a >= 0:
            return self.helper(a)
        else:
            temp = abs(a)-1
            #print temp

            return 32 - self.helper(temp)

    # helper()统计正数的二进制中1的个数
    def helper(self, n):
        count = 0
        while n != 0:
            n = n & (n - 1)
            #print n
            count += 1
        return count
