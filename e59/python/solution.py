class Solution:
    def threeSumClosest(self, numbers, target):
        # write your code here
        
        size = len(numbers)
        numbers.sort()
        sub = sum(numbers[:3])
        for i in range(size-2):
            left = i+1
            right = size-1
            while left < right:
                print numbers
                print i,left,right
                print numbers[i],numbers[left],numbers[right]
                tmp = numbers[i] + numbers[left] + numbers[right]
                if abs(tmp-target) < abs(sub-target):
                    sub = tmp
                if tmp < target:
                    left += 1
                else:
                    right -= 1
                print tmp,sub
        return sub

numbers = [1,2,33,23,2423,33,23,1,7,6,8787,5,33,2,3,-23,-54,-67,100,400,-407,-500,-35,-8,0,0,7,6,0,1,2,-56,-89,24,2]
print Solution().threeSumClosest(numbers, 148)
