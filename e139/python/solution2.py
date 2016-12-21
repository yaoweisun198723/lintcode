import sys
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
        sums = [(0, -1)]
        tmp = 0
        for i in range(len(nums)):
            tmp += nums[i]
            sums.append((tmp, i))
        sums.sort()
        diff = sys.maxint
        start = 0
        end = 0
        for j in range(1,len(sums)):
            if abs(sums[j][0] - sums[j-1][0]) < diff:
                diff = abs(sums[j][0] - sums[j-1][0])
                start = min(sums[j][1], sums[j-1][1])+1
                end = max(sums[j][1], sums[j-1][1])
        ret = [start, end]
        return ret
nums = [6,-4,-8,3,1,7]
print Solution().subarraySumClosest(nums)
