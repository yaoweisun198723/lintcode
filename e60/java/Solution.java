
public class Solution {
    /** 
     * param A : an integer sorted array
     * param target :  an integer to be inserted
     * return : an integer
     */
    public int searchInsert(int[] A, int target) {
        // write your code here
        if (A == null || A.length == 0) 
            return 0;
        if (target <= A[0])
            return 0;
        if (target > A[A.length - 1])
            return A.length;
        if (target == A[A.length - 1])
            return A.length - 1;
        int left = 0;
        int right = A.length - 1;
        while (right - left > 1) {
            int mid = (left + right) / 2;
            if (A[mid] < target)
                left = mid;
            else if (A[mid] > target)
                right = mid;
            else  //A[mid] == target
                return mid;
        }
        return left + 1;
    }
}
