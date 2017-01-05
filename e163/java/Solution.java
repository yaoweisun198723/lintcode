public class Solution {
    /**
     * @paramn n: An integer
     * @return: An integer
     */
    public int numTrees(int n) {
        // write your code here
        if (n < 0) {
            return -1;
        }
        if (n == 0 || n == 1) {
            return 1;
        }
        int[] nums = new int[n+1];
        nums[0] = 1;
        nums[1] = 1;

        for (int i=2; i<=n; i++) {
            int tmp = 0;
            for (int j=0; j<i; j++) {
                tmp += nums[j] * nums[i-1-j];
            }
            nums[i] = tmp;
        }
        return nums[n];
    }
}
