class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        # write your code here
        """Time Limit Exceeded
        n = len(gas)
        for start in range(n):
            r = 0
            loop = True
            for i in [station % n for station in range(start, start+n)]:
                #print i
                if (r + gas[i]) >= cost[i]:
                    r = r + gas[i] - cost[i]
                else:
                    loop = False
                    break
            if loop == True:
                return start
        return -1
        """
        n = len(gas)
        l = 0
        r = 0
        start = 0
        for i in range(n):
            diff = gas[i] - cost[i]
            if r < 0 and diff > 0:
                start = i
                l += r
                r = diff
            else:
                r += diff
        if (l + r) >= 0:
            return start
        else:
            return -1
