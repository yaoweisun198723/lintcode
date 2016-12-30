#class SVNRepo:
#    @classmethod
#    def isBadVersion(cls, id)
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can use SVNRepo.isBadVersion(10) to check whether version 10 is a 
# bad version.
class Solution:
    """
    @param n: An integers.
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        # write your code here
        if SVNRepo.isBadVersion(1):
            return 1
        if not SVNRepo.isBadVersion(n):
            return -1
        left = 1
        right = n
        while right - left > 1:
            mid = (left + right) / 2
            if SVNRepo.isBadVersion(mid):
                right = mid
            else:
                left = mid
        return right
