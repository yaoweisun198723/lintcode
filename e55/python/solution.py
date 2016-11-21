import sys
import getopt

class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def compareStrings(self, A, B):
        # write your code here
        dict_s = {}
        for c in A:
            if dict_s.has_key(c):
                dict_s[c] += 1
            else:
                dict_s[c] = 1

        for c in B:
            if dict_s.has_key(c):
                dict_s[c] -= 1
                if dict_s[c] < 0:
                    return False
            else:
                return False
        return True

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    if argv is None:
        argv = sys.argv
    print Solution().compareStrings("test", "tst")
    print Solution().compareStrings("test", "estt")

if __name__ == "__main__":
    sys.exit(main())
