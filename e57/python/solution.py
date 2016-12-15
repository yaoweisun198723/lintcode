import sys
class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        result = []
        last = []
        numbers.sort()
        for i in range(len(numbers)):
            if i == 0 or i >= 1 and numbers[i] != numbers[i-1]:
                left = i + 1
                right = len(numbers) - 1
                while left < right:
                    sum = numbers[i] + numbers[left] + numbers[right]
                    if sum == 0:
                        a = [numbers[i], numbers[left], numbers[right]]
                        if a != last:
                            result.append(a)
                            last = a
                        left += 1
                        right -= 1
                    elif sum > 0:
                        right -= 1
                    else:
                        left += 1
        return result

def main(argv=None):
    if argv is None:
        argv = sys.argv
    data = [-1,0,1,2,-1,-4]
    print Solution().threeSum(data)

if __name__ == '__main__':
    main()
