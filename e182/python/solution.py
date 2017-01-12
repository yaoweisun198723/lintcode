class Solution:
    """
    @param A: A positive integer which has N digits, A is a string.
    @param k: Remove k digits.
    @return: A string
    """
    def DeleteDigits(self, A, k):
        # write you code here
        n = len(A)
        ret_size = n - k
        ret = ''
        last_idx = -1
        for i in range(ret_size):
            minimal = 10
            for j in range(last_idx+1, i+k+1):
                tmp = int(A[j])
                if tmp < minimal:
                    minimal = tmp
                    last_idx = j
                    #print i,last_idx, minimal
            #print minimal
            ret += str(minimal)
        return ret.lstrip('0')
