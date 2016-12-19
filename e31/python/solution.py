import sys

class Solution:
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        # you should partition the nums by k
        # and return the partition index as description
        if len(nums) == 0:
            return 0
        lp = 0
        rp = len(nums) - 1
        while lp < rp:
            #print nums, lp, rp
            if nums[lp] < k:
                lp += 1
                continue
            if nums[rp] >= k:
                rp -= 1
                continue
            # swap two numbers
            tmp = nums[lp]
            nums[lp] = nums[rp]
            nums[rp] = tmp
            lp += 1
            rp -= 1

        if nums[lp] >= k:
            return lp
        else:
            return lp+1

def main(argv=None):
    if argv is None:
        argv = sys.argv
    nums = [9,9,9,8,9,8,7,9,8,8,8,9,8,9,8,8,6,9]
    print Solution().partitionArray(nums, 9)

if __name__ == '__main__':
    main()
