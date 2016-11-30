import sys

class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here
        origLen = len(A)
        newIdx = 0
        for i in range(origLen):
            if A[i] != elem:
                A[newIdx] = A[i]
                newIdx += 1
        del A[newIdx:]
        return newIdx

def main():
    lst = [0,0,4,4,2,3,4,5]
    print Solution().removeElement(lst, 4)

if __name__ == '__main__':
    sys.exit(main())
