class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    return: The maximum length of the small pieces.
    """
    def woodCut(self, L, k):
        # write your code here
        if sum(L) < k:
            return 0
        longest = max(L)
        if sum([x / longest for x in L]) >= k:
            return longest
        low = 1
        high = longest
        ret = 1
        while high - low > 1:
            mid = (low + high) / 2
            n = sum([x / mid for x in L])
            if n < k:
                high = mid
            else: #n >= k
                low = mid
                if mid > ret:
                    ret = mid
        return ret
