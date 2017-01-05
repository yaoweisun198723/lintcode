class Solution:
    # @paramn n: An integer
    # @return: An integer
    def numTrees(self, n):
        # write your code here
        # ref:http://blog.sina.com.cn/s/blog_5ce680a40102vqgu.html
        nums = [1, 1]
        if 0 <= n <= 1:
            return nums[n]
        if n < 0:
            return -1
        # n >= 2
        for i in range(2, n+1):
            tmp = 0
            for j in range(0, i):
                tmp += nums[j] * nums[i-1-j]
            nums.append(tmp)
        return nums[n]
