import sys

class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return 0

        j = 0
        value = A[0]
        for i in range(1, len(A)):
            if value != A[i]:
                j += 1
                A[j] = A[i]
                value = A[i]
        return j + 1

def main(argv=None):
    if argv is None:
        argv = sys.argv
    print Solution().removeDuplicates([1,1,2,2,3])
    print Solution().removeDuplicates(argv[1:])

if __name__ == '__main__':
    main()
