
public class Solution {
    /**
     * @param A: A list of integers
     * @return: The boolean answer
     */
    public boolean canJump(int[] A) {
        // wirte your code here
        int current_max = 0;
        for (int i=0; i<A.length-1; i++) {
            current_max = (current_max-1)>A[i]?(current_max-1):A[i];
            if (current_max == 0) {
                return false;
            }
        }
        return true;
    }
}
