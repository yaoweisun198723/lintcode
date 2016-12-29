public class Solution {
    /**
     * @param nums: a rotated sorted array
     * @return: the minimum number in the array
     */
    public int findMin(int[] nums) {
        // write your code here
        int size = nums.length;
        if (nums[0] < nums[size - 1]) {
            return nums[0];
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
        return nums[right];
    }
}
