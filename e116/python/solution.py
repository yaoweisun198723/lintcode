class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        # write your code here
        # 贪心算法
        """
        maxi = 0
        for i in range(len(A)-1):
            maxi = max(maxi-1, A[i])
            if maxi == 0:
                return False
        return True
        """
        # 动态规划
        canjump = [False for i in range(len(A))]
        canjump[-1] = True
        for i in range(len(A)-2, -1, -1):
            if A[i] == 0:
                canjump[i] = False
            elif A[i] + i >= len(A)-1:
                canjump[i] = True
            else:
                for j in range(i+1, i+A[i]+1):
                    if canjump[j] == True:
                        canjump[i] = True
                        break
                
        
        #print canjump
        return canjump[0]
