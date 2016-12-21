class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return 0
        value = A[0]
        count = 1
        newIdx = 0
        for i in range(1, len(A)):
            if A[i] != value:
                newIdx += 1
                A[newIdx] = A[i]
                value = A[i]
                count = 1
            else:
                count += 1
                if count <= 2:
                    newIdx += 1
                    A[newIdx] = A[i]
                    value = A[i]
                else:
                    pass
        return newIdx + 1
