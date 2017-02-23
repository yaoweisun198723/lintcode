class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        nums = set(nums)
        prefix = []
        self.result = []
        self.recursive(prefix, nums)
        return self.result

    def recursive(self, prefix, nums):
        if not nums:
            self.result.append(prefix[:])
#            print self.result
        else:
            for num in nums:
                prefix.append(num)
                self.recursive(prefix, nums - set([num]))
                prefix.pop()

data = []
#data = [1]
#data = [1,2]
print Solution().permute(data)
