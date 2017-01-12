public class Solution {
    /**
     * @param gas: an array of integers
     * @param cost: an array of integers
     * @return: an integer
     */
    public int canCompleteCircuit(int[] gas, int[] cost) {
        // write your code here
        int n = gas.length;
        int start = 0;
        int l = 0;
        int r = 0;
        int diff = 0;
        for (int i=0; i<n; i++) {
            diff = gas[i] - cost[i];
            if (r < 0 && diff > 0) {
                start = i;
                l += r;
                r = diff;
            }
            else {
                r += diff;
            }
        }
        if ((l+r) >= 0) {
            return start;
        }
        else {
            return -1;
        }
    }
}
