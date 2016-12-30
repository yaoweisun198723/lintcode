public class Solution {
    /** 
     *@param A : an integer rotated sorted array
     *@param target :  an integer to be searched
     *return : an integer
     */
    public int search(int[] A, int target) {
        // write your code here
        int size = A.length;
        if (size == 0) {
            return -1;
        }
        int shift = findMin(A);
        //System.out.println(shift);
        int l = 0;
        int r = size - 1;
        if (target == A[0+shift]) {
            return 0+shift;
        }
        if (target == A[(size-1+shift) % size]) {
            return (size-1+shift) % size;
        }
        while (r -l > 1) {
            int mid = (l + r) / 2;
            int realidx = (mid + shift) % size;
            int tmp = A[realidx];
            if (tmp == target) {
                return realidx;
            }
            else if (tmp > target) {
                r = mid;
            }
            else {
                l = mid;
            }
        }
        return -1;
    }
    
    /**
     * @param nums: a rotated sorted array
     * @return: the minimum number in the array
     */
    public static int findMin(int[] nums) {
        // write your code here
        int size = nums.length;
        if (nums[0] < nums[size - 1]) {
            return 0;
        }
        int left = 0;
        int right = size - 1;
        while (right - left > 1) {
            int mid = (left + right) / 2;
            if (nums[mid] > nums[right]) {
                left = mid;
            }
            else {
                right = mid;
            }
        }
        return right;
    }
}
