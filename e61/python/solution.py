class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        size = len(A)
        if size == 0:
            return [-1, -1]

        #find index1
        l = 0
        r = size - 1
        index1 = -1

        if A[0] == target:
            index1 = 0
        else:
            if A[size-1] == target:
                index1 = size - 1
            while r - l > 1:
                m = (l + r) / 2
                if A[m] < target:
                    l = m
                elif A[m] > target:
                    r = m
                else: #A[m] == target
                    r = m
                    index1 = m
        #find index2
        l = 0
        r = size - 1
        index2 = -1

        if A[size-1] == target:
            index2 = size - 1
        else:   
            if A[0] == target:
                index2 = 0
            while r - l > 1:
                m = (l + r) / 2
                if A[m] > target:
                    r = m
                elif A[m] < target:
                    l = m
                else: #A[m] == target
                    l= m
                    index2 = m
            
        return [index1, index2]
        
