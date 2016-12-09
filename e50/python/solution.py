class Solution:
    """
    @param A: Given an integers array A
    @return: An integer array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, A):
        # write your code here 
        nMulti = len(A) - 1
        if nMulti == 1:
            return [1]
        l = []
        while nMulti > 1:
            q = nMulti / 2
            r = nMulti % 2
            l.append((q, r))
            nMulti = q
        l.reverse()
        m = [ [0] *len(A) for row in range(len(l)+1)]
        m[0] = A
        for i in range(len(l)):
            for j in range(len(A)):
                q = l[i][0]
                r = l[i][1]
                if r == 0:
                    #print i,j
                    #print 'before modify:' + str(m)
                    m[i+1][j] = m[i][j] * m[i][(j+q) % len(A)]
                    #print 'after modify:' + str(m)
                else:
                    #print i,j
                    #print 'before modify:' + str(m)
                    m[i+1][j] = m[i][j] * m[i][(j+q) % len(A)] * m[0][(j+q*2) % len(A)]
                    #print 'after modify:' + str(m)

        ret = [0] * len(A)
        for i in range(len(A)):
            ret[i] = m[len(l)][(i+1) % len(A)]
        return ret

def main(argv=None):
    nums = [1,2,3,4,5,6,7]
    nums = [1,2,3,4,5,6]
    nums = [1,2]
    nums = [2]
    print Solution().productExcludeItself(nums)

if __name__ == '__main__':
    main()
