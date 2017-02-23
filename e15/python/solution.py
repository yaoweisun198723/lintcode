class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        """
        res = []
        if not nums:
            return [[]]
        if len(nums) == 1:
            res.append(nums)
            return res
        first = nums[0]    
        last = self.permute(nums[1:])
        for x in last:
            for i in range(len(nums)):
                tmp = x[:]
                tmp.insert(i, first)
                res.append(tmp)
        return res
        """
        length = len(nums)
        index = 0
        curr_level = [[]]
        while index < length:
            pre_level = curr_level
            curr_level = []
            for permute in pre_level:
                for j in range(index+1):
                    tmp = permute[0:j] + [nums[index]] + permute[j:]
                    curr_level.append(tmp)
            index += 1
        return curr_level

data = [1,2,3]
print Solution().permute(data)
