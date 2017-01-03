class Solution:
    """
    @param matrix: An list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicates the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if matrix is None or len(matrix) == 0:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        x = m - 1
        y = 0
        count = 0
        while x >= 0 and y <= n - 1:
            if matrix[x][y] > target:
                x -= 1
            elif matrix[x][y] < target:
                y += 1
            else: #matrix[x][y] == target
                count += 1
                x -= 1
                y += 1
        return count
