import sys

class Solution:
    # @param strs: A list of strings
    # @return: The longest common prefix
    def longestCommonPrefix(self, strs):
        # write your code here
        if not strs or len(strs) == 0:
            return ""
        minLen = min([len(s) for s in strs])
        ret = ""
        for i in range(minLen):
            tmp = strs[0][i]
            same = True
            for s in strs:
                if tmp != s[i]:
                    same = False
                    return ret
            if same == True:
                ret += tmp;
        return ret

def main(argv=None):
    if argv is None:
        argv = sys.argv
    print argv[1:]
    print Solution().longestCommonPrefix(argv[1:])

if __name__ == '__main__':
    sys.exit(main())
