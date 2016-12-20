import sys
class Solution:
    # @param str: a string
    # @return an integer
    def atoi(self, str):
        # write your code here
        if str is None or str == "":
            return 0
        str = str.strip()
        sign = 1
        if str[0] == '-':
            sign = -1
            str = str[1:]
        elif str[0] == '+':
            str = str[1:]
        else:
            pass

        ints = []
        digits = []
        points = 0
        for c in str:
            if c >= '0' and c <= '9':
                ints.append(c)
            else:
                break
        if ints == []:
            return 0

        ret = 0
        for i in range(len(ints)):
            ret += (ord(ints[i]) - ord('0')) * 10 ** (len(ints)-1-i)
        if ret > 2147483647 and sign == 1:
            return 2147483647
        if ret > 2147483648 and sign == -1:
            return -2147483648

        return sign * ret

print Solution().atoi("  -51235")
print Solution().atoi(sys.argv[1])
