class Solution:
    """
    @param nums: A list of integers.
    @return: A list of unique permutations.
    """
    # non-recursive
    def permuteUnique(self, nums):
        pre_permute = [[]]
        for number in nums:
            cur_permute = []
            for per in pre_permute:
                for i in range(len(per)+1):
                    tmp = per[:]
                    tmp.insert(i,number)
                    if tmp not in cur_permute:
                        cur_permute.append(tmp)
            pre_permute = cur_permute
        return pre_permute
