import sys
import getopt

class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        # write your code here
        longer = A if len(A) > len(B) else B
        shorter = A if len(A) <= len(B) else B
        for max_len in range(len(shorter), 0, -1):
            for i in range(0, len(shorter)-max_len+1):
                for j in range(0, len(longer)-max_len+1):
                    if longer[j:j+max_len] == shorter[i:i+max_len]:
                        return max_len
        return 0

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    if argv is None:
        argv = sys.argv
    print Solution().longestCommonSubstring("aabcdefghde", "def")

if __name__ == "__main__":
    sys.exit(main())
