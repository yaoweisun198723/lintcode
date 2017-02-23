class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    def subsets(self, S):
        # write your code here
        S.sort()
        return self.recursive(S)
        
    def recursive(self,S):
        if not S:
            return [[]]
        #if len(S) == 1:
        #    return [S]
        head = S[0:1]
        new_sets = []
        pre_level_sets = self.recursive(S[1:])
        for set in pre_level_sets:
            tmp = head + set
            new_sets.append(tmp)
        return pre_level_sets + new_sets
