class Solution:
    """
    Get all distinct N-Queen solutions
    @param n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        self.n = n
        self.result = []
        prefix = []
        self.reverse(prefix, 0)
        return self.convert(self.result)
    
    def reverse(self, prefix, row):
        if row < self.n:
            newq = [row, None]
            for col in range(self.n):
                newq[1] = col
                can_attack = self.canAttack(prefix, newq)
                if can_attack:
                    continue
                else:
                    prefix.append(newq[:])
                    self.reverse(prefix, row+1)
                    prefix.pop()
        elif row == self.n:
            self.result.append(prefix[:])
        else: #row > self.n
            pass

    def canAttack(self, prefixQueen, newQueen):
        if prefixQueen == None:
            return False
        for q in prefixQueen:
            if q[1] - q[0] == newQueen[1] - newQueen[0] or \
                q[0] - newQueen[0] == newQueen[1] - q[1] or \
                q[1] == newQueen[1] or \
                q[0] == newQueen[0]:
                return True
        return False

    def convert(self, solutions):
        result = []
        for coords in solutions:
            solution = []
            for cod in coords:
                tmp = ['.'] * self.n
                tmp[cod[1]] = 'Q'
                solution.append(''.join(tmp))
            result.append(solution)
        return result
print Solution().solveNQueens(4)
