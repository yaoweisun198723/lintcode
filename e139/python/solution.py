class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    def subarraySumClosest(self, nums):
        # write your code here
        """
        diff = abs(nums[0])
        ret = [0, 0]
        for i in range(len(nums)):
            sum = nums[i]
            if abs(sum) < diff:
                diff = abs(sum)
                ret = [i, i]
            for j in range(i+1, len(nums)):
                sum += nums[j]
                if abs(sum) < diff:
                    diff = abs(sum)
                    ret = [i, j]
        return ret
        """
        if nums is None or len(nums)==0:
            return []
        if len(nums) == 1:
            return [0, 0]
        sums = []
        tmp = 0
        for i in range(len(nums)):
            tmp += nums[i]
            sums.append((tmp, i))
        sums.sort()
        diff = abs(sums[0][0] - sums[1][0])
        start = min(sums[0][1], sums[1][1])+1
        end = max(sums[0][1], sums[1][1])
        ret = [start, end]
        for j in range(1,len(sums)):
            if sums[j][0] == 0:
                return [0, sums[j][1]]
            if abs(sums[j][0] - sums[j-1][0]) < diff:
                diff = abs(sums[j][0] - sums[j-1][0])
                start = min(sums[j][1], sums[j-1][1])+1
                end = max(sums[j][1], sums[j-1][1])
        ret = [start, end]
        return ret
nums = [6,-4,-8,3,1,7]
print Solution().subarraySumClosest(nums)
