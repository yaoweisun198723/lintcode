class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        # write your code here
        if A is None or len(A) == 0:
            return -1
        l = 0
        r = len(A) - 1
        t = target
        if target == A[0]:
            return 0
        if target == A[len(A)-1]:
            return len(A) - 1
        while r - l > 1:
            m = (l + r) / 2
            if A[l] < A[m] < A[r] < t or \
               A[r] < t < A[l] < A[m] or \
               A[m] < A[r] < t < A[l] or \
               t < A[l] < A[m] < A[r]:
                return -1
            if t == A[m]:
                return m
            elif A[l] < A[m] < t < A[r] or \
                 A[r] < A[l] < A[m] < t or \
                 A[m] < t < A[r] < A[l] or \
                 t < A[r] < A[l] < A[m]:
                l = m
            else:
                r = m
        return -1
                
