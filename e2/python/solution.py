class Solution:
    # @param n a integer
    # @return ans a integer
    def trailingZeros(self, n):
        zeros = 0
        radix = 5
        while True:
            tmp = n / radix
            if tmp == 0:
                return zeros
            zeros += tmp
            radix *= 5
