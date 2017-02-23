class Solution:
    """
    @param S: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, S):
        # write your code here
        numbers = S[:]
        numbers.sort()
        subsets = [[]]
        for num in S:
            newsets = []
            single = [num]
            for subset in subsets:
                tmp = subset + single
                if tmp not in subsets:
                    newsets.append(tmp)
            subsets += newsets
        return subsets

print Solution().subsetsWithDup([1,2,2])
