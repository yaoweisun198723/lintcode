class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        # write your code here
        size = len(A)
        B = [0] * size

        for i in range(size):
            if A[i] >= 1 and A[i] <= size:
                B[A[i]-1] = A[i]

        for i in range(size):
            if B[i] == 0:
                return i+1

        return size+1


def main():
    A = [1,2,0]
    print Solution().firstMissingPositive(A)

if __name__ == '__main__':
    main()


