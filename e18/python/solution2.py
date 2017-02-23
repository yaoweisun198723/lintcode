class Solution:
    """
    @param S: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, S):
        S.sort()
        return self.recursive(S)
        
    def recursive(self, S):
        if not S:
            return [[]]
        if len(S) == 1:
            return [[],S]
        pre_level_set = self.recursive(S[1:])
        new_set = []
        single = S[0:1]
        for subset in pre_level_set:
            tmp = single + subset
            if tmp not in pre_level_set:
                new_set.append(tmp)
        cur_level_set = new_set + pre_level_set
        return cur_level_set

print Solution().subsetsWithDup([1,2,2,2])
