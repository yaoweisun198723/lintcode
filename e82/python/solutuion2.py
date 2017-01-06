class Solution:
    """
    @param A : an integer array
    @return : a integer
    """
    def singleNumber(self, A):
        # write your code here
        if A is None or A == []:
            return 0
        possible = {}
        for num in A:
            if possible.has_key(num):
                del possible[num]
            else:
                possible[num] = 1
        return possible.keys()[0]
