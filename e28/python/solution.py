class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if matrix is None or matrix == []:
            return False
        m = len(matrix)
        n = len(matrix[0])
        #locate line
        firstColumn = [matrix[line][0] for line in range(m)]
        if target < firstColumn[0]:
            return False
        if target > firstColumn[-1]:
            possibleLine = matrix[-1]
        else:
            left = 0
            right = m - 1
            while right - left > 1:
                mid = (left + right) / 2
                if firstColumn[mid] == target:
                    return True
                elif firstColumn[mid] < target:
                    left = mid
                else:
                    right = mid
            possibleLine = matrix[left]
        
        #locate column
        l = 0
        r = n - 1

        if target < possibleLine[0] or target > possibleLine[-1]:
            return False
        if target == possibleLine[0] or target == possibleLine[-1]:
            return True
        while r - l > 1:
            mid = (l + r) / 2
            if possibleLine[mid] == target:
                return True
            elif possibleLine[mid] < target:
                l = mid
            else:
                r = mid
        return False
