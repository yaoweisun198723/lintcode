class Solution:
    """
    @param numbersbers : Give an array numbersbersbers of n integer
    @param target : you need to find four elements that's sum of target
    @return : Find all unique quadruplets in the array which gives the sum of 
              zero.
    """
    def fourSum(self ,numbers, target):
        # write your code here
        numbers.sort()
        ret = {}
        for first in range(len(numbers) - 3):
            for second in range(first+1, len(numbers)-2):
                third = second + 1
                fourth = len(numbers) - 1
                while third < fourth:
                    tmp = numbers[first] + numbers[second] + numbers[third] +\
                          numbers[fourth]
                    if tmp > target:
                        fourth -= 1
                    elif tmp < target:
                        third += 1
                    else:
                        key = (numbers[first], numbers[second],\
                            numbers[third], numbers[fourth])
                        ret[key] = 1
                        third += 1
                        fourth -= 1
        return ret.keys()

nums = [1,0,-1,-1,-1,-1,0,1,1,1,2]
target = 2
print Solution().fourSum(nums, target)

