class Solution:
    """
    @param A: sorted integer array A which has m elements, 
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        idxA = m - 1
        idxB = n - 1
        for i in range(m+n-1, -1, -1):
            if idxA < 0:
                A[i] = B[idxB]
                idxB -= 1
            elif idxB < 0:
                A[i] = A[idxA]
                idxA -= 1
            elif A[idxA] < B[idxB]:
                A[i] = B[idxB]
                idxB -= 1
            else:
                A[i] = A[idxA]
                idxA -= 1
