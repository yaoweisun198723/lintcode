class Solution:
    def productExcludeItself(self, A):
        ret = []
        for i in range(len(A)):
            product = 1
            for j in range(len(A)):
                if j != i:
                    product *= A[j]
            ret.append(product)
        return ret
