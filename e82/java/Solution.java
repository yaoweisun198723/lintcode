public class Solution {
    /**
      *@param A : an integer array
      *return : a integer 
      */
    public int singleNumber(int[] A) {
        // Write your code here
        int res = 0;
        for (int i:A) {
            res = res ^ i;
        }
        return res;
    }
}
