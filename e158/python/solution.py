import sys
import getopt

class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        # write your code here
        if len(s) != len(t):
            return False

        dict_s = {}
        for c in s:
            if dict_s.has_key(c):
                dict_s[c] += 1
            else:
                dict_s[c] = 1

        dict_t = {}
        for c in t:
            if dict_t.has_key(c):
                dict_t[c] += 1
            else:
                dict_t[c] = 1

        for c in s:
            if (not dict_t.has_key(c) or dict_s[c] != dict_t[c]):
                return False

        return True

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    if argv is None:
        argv = sys.argv
    print Solution().anagram("test", "tstee")
    print Solution().anagram("test", "estt")

if __name__ == "__main__":
    sys.exit(main())
