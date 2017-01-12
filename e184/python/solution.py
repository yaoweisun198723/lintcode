class Solution:	
    #@param num: A list of non negative integers
    #@return: A string
    def largestNumber(self, num):
        # write your code here
        num.sort(cmp=self.compare)
        ret = ''
        for i in num:
            ret += str(i)
        if int(ret) == 0:
            ret = '0'
        return ret
    
    def compare(self,x, y):
        strx = str(x)
        stry = str(y)
        n = min(len(strx), len(stry))

        equal = 0
        for i in range(n):
            if strx[i] > stry[i]:
                equal = 1
                break
            elif strx[i] < stry[i]:
                equal = -1
                break
            else:
                continue
                            
        if equal == 0 and len(strx) != len(stry):
            if len(strx) > len(stry):
                if strx[n] > strx[0]:
                    equal = 1
                elif strx[n] < strx[0]:
                    equal = -1
                else:
                    equal = 0
            else:
                if stry[n] > stry[0]:
                    equal = -1
                elif stry[n] < stry[0]:
                    equal = 1
                else:
                    equal = 0
        return equal * -1
            
