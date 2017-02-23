class Solution:
    """
    @param nums: A list of integers.
    @return: A list of unique permutations.
    """
    # recursive
    def permuteUnique(self, nums):
        # write your code here
        if not nums:
            return [[]]
        if len(nums) == 1:
            return [nums]
        number = nums[0]
        cur_permute = []
        pre_permute = self.permuteUnique(nums[1:])
        for per in pre_permute:
            for i in range(len(per)+1):
                tmp = per[:]
                tmp.insert(i,number)
                if tmp not in cur_permute:
                    cur_permute.append(tmp)
        return cur_permute
