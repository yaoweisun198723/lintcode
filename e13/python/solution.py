import sys


class Solution:
    def strStr(self, source, target):
        # write your code here
        if source is None or target is None:
            return -1

        if target == "":
            return 0
        if len(source) < len(target):
            return -1
        index = 0
        equal = 0
        for i in range(len(source) - len(target) + 1):
            index = i
            equal = 0
            for j in range(len(target)):
                if source[i+j] == target[j]:
                    equal += 1
                else:
                    break
            if equal == len(target):
                return index
        return -1
#       return source.find(target)

def main(argv=None):
    if argv is None:
        argv = sys.argv
    print Solution().strStr("abcdefg", "bcd")
    print Solution().strStr("abcdefg", "fg")
    print Solution().strStr("abcdefg", "g")
    print Solution().strStr("", "bcd")
    print Solution().strStr("abcd", "")
    print len(sys.argv)

if __name__ == "__main__":
    sys.exit(main())
