public class Solution {
    /** 
     *@param L: Given n pieces of wood with length L[i]
     *@param k: An integer
     *return: The maximum length of the small pieces.
     */
    public int woodCut(int[] L, int k) {
        // write your code here
        long sum = 0L;
        int longest = 0;
        for (int wood:L) {
            sum += (long)wood;
            if (wood > longest) {
                longest = wood;
            }
        }
        if (sum < (long)k) { //length = 1
            return 0;
        }
        if (divide(L, longest) >= k) {
            return longest;
        }

        int ret = 1;
        int low = 1;
        int high = longest;
        while (high - low > 1) {
            int mid = low / 2 + high / 2 + (low % 2 + high % 2) / 2;
            if (divide(L, mid) < k) {
                high = mid;
            }
            else {
                low = mid;
            }
        }
        return low;
    }
    public int divide(int[] L, int length) {
        int k = 0;
        for (int wood:L) {
            k += wood / length;
        }
        return k;
    }
}
