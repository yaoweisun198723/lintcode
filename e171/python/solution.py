import sys
import getopt

class Solution:

    def tomap(self, str):
        map = {}
        for c in str:
            if map.has_key(c):
                map[c] += 1
            else:
                map[c] = 1
        return map

    """
    # @param strs: A list of string
    # @return: A list of string
    """
    def anagrams(self, strs):
        # write your code here
        ret = []
        size = len(strs)
        strmaps = [self.tomap(str) for str in strs]
        flags = [0] * size
        for i in range(size):
            if (flags[i] == 1):
                continue
            count = 0
            for j in range(i+1, size):
                if (flags[j] == 1):
                    continue
                if (strmaps[i] == strmaps[j]):
                    ret.append(strs[j])
                    flags[j] = 1
                    count += 1
            if count > 0:
                ret.append(strs[i])

        #for i in range(size):
        #    if flags[i] == 1:
        #        ret.append(strs[i])

        return ret


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    if argv is None:
        argv = sys.argv
    print Solution().anagrams(['hello', 'olleh', 'abcd','lleoh', 'bcd', 'dcba'])
    print Solution().anagrams(argv)
    #strmaps = [Solution().tomap(str) for str in argv]


if __name__ == "__main__":
    sys.exit(main())
