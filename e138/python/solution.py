import sys

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        """Time Limit Exceeded
        for subLen in range(1, len(nums)+1):
            for first in range(len(nums)-subLen+1):
                if sum(nums[first:first+subLen]) == 0:
                    return list((first, first+subLen-1))
        """
        """Time Limit Exceeded
        for first in range(len(nums)):
            for subLen in range(1, len(nums)+1-first):
                if sum(nums[first:first+subLen]) == 0:
                    return list((first, first+subLen-1))
        return []
        """
        #"""Correct Answer
        for first in range(len(nums)):
            subsum = nums[first]
            if subsum == 0:
                return list((first, first))
            for last in range(first+1, len(nums)):
                subsum += nums[last]
                if subsum == 0:
                    return list((first, last))
        print count
        return []
        """
        iterSum = [0] * (len(nums)+1)
        for subLen in range(1, len(nums)+1):
            for idx in range(len(nums)+1-subLen):
                count += 1
                iterSum[idx] = nums[idx] + iterSum[idx+1]
                if iterSum[idx] == 0:
                    return list((idx, idx+subLen-1))
        return []
        """

def main(argv=None):
    if argv is None:
        argv = sys.argv
    #print argv
    #nums = [int(x) for x in argv[1:]]
    file = open('../data.in', 'r')
    data  = file.read()
    file.close()
    nums = [int(x) for x in data[1:-1].split(',')]
    print Solution().subarraySum(nums);
    #print Solution().subarraySum(range(1,11));
    #print sum(nums[1:16005])
    #print len(nums)


if __name__ == '__main__':
    main()
