class Solution:
    #@param A: An integers list.
    #@return: return any of peek positions.
    def findPeak(self, A):
        # write your code here
        for i in range(1, len(A)-1):
            if A[i-1] < A[i] > A[i+1]:
                return i
