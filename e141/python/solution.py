class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        left = 1
        right = x
        while (left <= right):
            if left ** 2 <= x and (left+1) ** 2 > x:
                return left
            mid = (left + right) / 2
            if mid ** 2 < x:
                left = mid
            elif mid ** 2 > x:
                right = mid
            else:
                return mid
        return 0
