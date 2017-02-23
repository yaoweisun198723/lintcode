class Solution:
    """    
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n   
    """
    def combine(self, n, k):      
        if k <= 0 or n < k:
            return []
        self.result = []
        prefix = []
        self.dfs(prefix, n, k)
        return self.result
    def dfs(self, prefix, n, k):
        if k < 0:
            return
        elif k == 0:
            tmp = prefix[:]
            tmp.reverse()
            self.result.append(tmp)
        else: # k >0
            for i in range(n, 0, -1):
                prefix.append(i)
                self.dfs(prefix, i-1, k-1)
                prefix.pop()
