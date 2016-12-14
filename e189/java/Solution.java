public class Solution {
    /**    
     * @param A: an array of integers
     * @return: an integer
     */
    public int firstMissingPositive(int[] A) {
        // write your code here   
        int len = A.length;
        int[] flag = new int[len];
        for (int i=0; i < len; i++) {
            if (A[i] >= 1 & A[i] <= len) {
                flag[A[i] - 1] = 1;
            }
        }
        
        for (int j=0; j < len; j++) {
            if (flag[j] == 0) {
                return j+1;
            }
        }
        return len+1;
    }
}
