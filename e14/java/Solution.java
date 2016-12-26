class Solution {
    /**
     * @param nums: The integer array.
     * @param target: Target to find.
     * @return: The first position of target. Position starts from 0.
     */
    public int binarySearch(int[] nums, int target) {
        //write your code here
        int size = nums.length;
        if (target < nums[0] || target > nums[size-1]) {
            return -1;
        }
        int left = 0;
        int right = size - 1;
        while (right -left > 1) {
            int mid = (left + right) / 2;
            if (nums[mid] >= target) {
                right = mid;
            }
            else {
                left = mid;
            }
        }
        if (nums[left] == target) {
            return (int)left;
        }
        else if (nums[right] == target) {
            return (int)right;
        }
        else {
            return -1;
        }
    }
}
