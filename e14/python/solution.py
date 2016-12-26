class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    def binarySearch(self, nums, target):
        # write your code here
        if target < nums[0] or target > nums[-1]:
            return -1
        left = 0
        right = len(nums) - 1

        while right - left > 1:
            mid = (left + right) / 2
            if nums[mid] >= target:
                right = mid
            else: #nums[mid] < target:
                left = mid
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1
        
