public class Solution {
    /** 
     * param A : an integer ratated sorted array and duplicates are allowed
     * param target :  an integer to be search
     * return : a boolean 
     */
    public boolean search(int[] A, int target) {
        // write your code here
        int size = A.length;    
        for(int i=0; i<size; i++) {
            if (A[i] == target) {
                return true;
            }
        }
        return false;
    }
}
