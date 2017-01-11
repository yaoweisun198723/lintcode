class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        """
        count_dict = {}
        for num in nums:
            if count_dict.has_key(num):
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        
        max_key = 0
        max_count = 0
        for k,v in count_dict.items():
            if v > max_count:
                max_count = v
                max_key = k
        return max_key
        """
        # ref:http://blog.csdn.net/gukesdo/article/details/7585636
        count = 0
        major = None
        
        for num in nums:
            if count == 0:
                major = num
                count = 1
            else:
                if num == major:
                    count += 1
                else:
                    count -= 1
        #print major
        return major
            
