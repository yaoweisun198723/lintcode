import sys
class Solution:
    #@param A and B: sorted integer array A and B.
    #@return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        # write your code here
        ret = []
        sza = len(A)
        szb = len(B)
        pa = 0
        pb = 0
        for i in range(sza + szb):
            if pa == sza:
                ret.append(B[pb])
                pb += 1
            elif pb == szb:
                ret.append(A[pa])
                pa += 1
            else:
                if A[pa] < B[pb]:
                    ret.append(A[pa])
                    pa += 1
                else:
                    ret.append(B[pb])
                    pb += 1
        return ret

def main(argv=None):
    if argv is None:
        argv = sys.argv
    lista = range(1, 10000000)
    #lista = range(0, 10)
    listb = [1,3,5]
    Solution().mergeSortedArray(lista, listb)


if __name__ == '__main__':
    main()
