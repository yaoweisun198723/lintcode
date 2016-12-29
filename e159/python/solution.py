class Solution:
    # @param nums: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, nums):
        # write your code here
        """ Solution 1, O(n)
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                return nums[i+1]
        return nums[0]
        """
        # Solution 2, O(logn)
        if nums[0] < nums[-1]:
            return nums[0]

        left = 0
        right = len(nums) - 1
        while right - left > 1:
            mid = (left + right) / 2
            if nums[mid] > nums[right]:
                left = mid
            else:
                right = mid
        return nums[right]
