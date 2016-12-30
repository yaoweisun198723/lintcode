class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        # write your code here
        size = len(num)
        if size is None or size == 0:
            return None
        if num[0] < num[-1]:
            return num[0]
        left = 0
        right = size - 1
        while right - left > 1:
            #print left, right
            mid = (left + right) / 2
            if num[mid] > num[left] or \
               num[mid] == num[left] and num[mid] > num[right]:
                left = mid
            elif num[mid] < num[right] or \
                 num[mid] == num[right] and num[mid] < num[left]:
                right = mid
            else: #num[mid] == num[left] == num[right]
                break
       
        if right - left > 1:
            #print left, right
            minNum = num[left]
            for i in range(left+1, right):
                if num[i] < minNum:
                    minNum = num[i]
            return minNum
        else:
            return num[right]
