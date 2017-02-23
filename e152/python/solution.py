class Solution:
    """    
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n   
    """
    def combine(self, n, k):      
        # write your code here
        if k <=0 or k > n:
            return []

        if k == 1:
            return [[i] for i in range(1, n+1)]
        # k > 1
        result = []
        for i in range(n, 1, -1):
            last_level = self.combine(i-1, k-1)
            result += [ e + [i] for e in last_level]
        return result

print Solution().combine(4,3)
