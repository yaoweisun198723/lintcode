class Solution:
    """
    @param A : an integer ratated sorted array and duplicates are allowed
    @param target : an integer to be searched
    @return : a boolean
    """
    def search(self, A, target):
        # write your code here
        #"""
        if A is None or len(A) == 0:
            return False
        l = 0
        r = len(A) - 1
        t = target
        if target == A[0]:
            return True
        if target == A[len(A)-1]:
            return True
        while r - l > 1:
            m = (l + r) / 2
            #print l,r,m
            if t == A[m]:
                return True
            elif A[l] == A[r] == A[m]:
                #"""
                if self.search(A[l+1:m],target) or \
                   self.search(A[m+1:r], target):
                    return True
                """
                for i in range(l+1, r):
                    if A[i] == target:
                        return True
                return False
                """
            elif A[l] <= A[m] <= A[r] < t or \
               A[r] < t < A[l] <= A[m] or \
               A[m] <= A[r] < t < A[l] or \
               t < A[l] <= A[m] <= A[r]:
                return False

            elif A[l] <= A[m] < t < A[r] or \
                 A[r] <= A[l] <= A[m] < t or \
                 A[m] < t < A[r] <= A[l] or \
                 t < A[r] <= A[l] <= A[m]:
                l = m
            else:
                r = m
        return False
        """
        for i in range(len(A)):
            if A[i] == target:
                return True
        return False
        """
