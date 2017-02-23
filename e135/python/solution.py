class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        # write your code here
        candidates.sort()
        candidates = self.deleteDuplicate(candidates)
        self.target = target
        self.result = []
        prefix = []
        self.reverse(prefix, candidates)
        return self.result

    def reverse(self, prefix, candidates):
        #print self.result, prefix, candidates
        pfx_sum = sum(prefix)
        if pfx_sum == self.target:
            self.result.append([e for e in prefix])
        elif pfx_sum < self.target:
            for i in range(len(candidates)):
                c = candidates[i]
                prefix.append(c)
                self.reverse(prefix, candidates[i:])
                if sum(prefix) >= self.target:
                    prefix.pop()
                    break
                else:
                    prefix.pop()
        else: #pfx_sum > self.target
            pass
        #print self.result, prefix, candidates

    def deleteDuplicate(self, nums):
        result = []
        last = -1
        for c in nums:
            if c != last:
                result.append(c)
                last = c
        return result


if __name__ == '__main__':
    #print Solution().combinationSum([2, 2, 3], 7)
    print Solution().combinationSum([2,3,6,7], 7)
