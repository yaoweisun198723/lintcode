class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        # write your code here
        if A is None or len(A) == 0:
            return 0
        if target <= A[0]:
            return 0
        if target > A[-1]:
            return len(A)
        if target == A[-1]:
            return len(A) - 1
        left = 0
        right = len(A) - 1
        while right - left > 1:
            mid = (left+right) / 2
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                left = mid
            else: #A[mid] > target
                right = mid

        return left + 1
