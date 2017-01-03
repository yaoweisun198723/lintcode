class Solution:
    """
    @param a, b: Two integer
    return: An integer
    """
    #"""
    def bitSwapRequired(self, a, b):
        # write your code here
        xor = a ^ b
        count = 0
        shift = 1
        for i in range(32):
            if xor & shift << i:
                count += 1

        return count
