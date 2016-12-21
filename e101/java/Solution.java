public class Solution {
    /**
     * @param A: a array of integers
     * @return : return an integer
     */
    public int removeDuplicates(int[] nums) {
        // write your code here
        if (nums == null || nums.length == 0)
            return 0;
        int value = nums[0];
        int count = 1;
        int j = 0;
        
        for (int i=1; i<nums.length; i++) {
            if (nums[i] != value) {
                j++;
                nums[j] = nums[i];
                value = nums[i];
                count = 1;
            }
            else { //nums[i] == value
                count++;
                if (count <= 2) {
                    j++;
                    nums[j] = nums[i];
                    value = nums[i];
                }
                else { //count > 2
                    continue;
                }
            }
        }

        return j+1;
    }
}
