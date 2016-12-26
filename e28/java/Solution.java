public class Solution {
    /**
     * @param matrix, a list of lists of integers
     * @param target, an integer
     * @return a boolean, indicate whether matrix contains target
     */
    public boolean searchMatrix(int[][] matrix, int target) {
        // write your code here
        if (matrix == null || matrix.length == 0) {
            return false;
        }
        int m = matrix.length;
        int n = matrix[0].length;
        if (target < matrix[0][0] || target > matrix[m-1][n-1]) {
            return false;
        }
        //locate line
        int left = 0;
        int right = m - 1;
        int possibleLine = 0;
        if (target > matrix[m-1][0]) {
            possibleLine = m - 1;
        }
        else {
            while (right - left > 1) {
                int mid = (left + right) / 2;
                if (matrix[mid][0] <= target) {
                    left = mid;
                }
                else {
                    right = mid;
                }
            }
            possibleLine = left;
        }
        //locate column
        if (target == matrix[possibleLine][0] || target ==                                matrix[possibleLine][n-1]) {
            return true;
        }
        int l = 0;
        int r = n - 1;
        while (r - l > 1) {
            int midd = (l + r) / 2;
            if (matrix[possibleLine][midd] == target) {
                return true;
            }
            else if (matrix[possibleLine][midd] < target) {
                l = midd;
            }
            else {
                r = midd;
            }
        }
        return false;
    }
}
