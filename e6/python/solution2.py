import sys
class Solution:
    #@param A and B: sorted integer array A and B.
    #@return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        if len(A) > len(B):
            shortArray = B
            longArray = A
        else:
            shortArray = A
            longArray = B
        newbegin = 0
        ret = []
        for i in range(len(shortArray)):
            e = shortArray[i]
            if e <= longArray[newbegin]:
                ret.append(e)
            elif e >= longArray[-1]:
                ret += longArray[newbegin:]
                ret += shortArray[i:]
                newbegin = len(longArray)
                break
            else:
                tmp = self.find(longArray, e)
                ret += longArray[newbegin:tmp]
                ret.append(e)
                newbegin = tmp

        if newbegin < len(longArray):
            ret += longArray[newbegin:]
        return ret


    def find(self, array, element):
        #make sure element  between min and max of array
        if element <= array[0]:
            return 0
        if element >= array[-1]:
            return len(array)
        lp = 0
        rp = len(array) - 1
        while rp - lp > 1:
            if array[(lp + rp) / 2] > element:
                rp = (lp + rp) / 2
            else:
                lp = (lp + rp) / 2
        return rp


def main(argv=None):
    if argv is None:
        argv = sys.argv
    lista = range(1, 10000000)
    #lista = range(0, 10)
    listb = [1,3,5]
    Solution().mergeSortedArray(lista, listb)


if __name__ == '__main__':
    main()
