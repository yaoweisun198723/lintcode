public class Solution {
    /**
     * @param A: a array of integers
     * @return : return an integer
     */
    public int removeDuplicates(int[] nums) {
        // write your code here
        if (nums == null || nums.length == 0)
            return 0;

        int j = 0;
        int value = nums[0];
        for (int i=1; i < nums.length; i++) {
            if (value != nums[i]) {
                j++;
                nums[j] = nums[i];
                value = nums[i];
            }
        }
        return j + 1;
    }

	public static void main(String[] args) {

		int[] nums = {1,1,2,2,3};
		new Solution().removeDuplicates(nums);
	}
}
