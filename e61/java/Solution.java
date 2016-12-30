
public class Solution {
    /** 
     *@param A : an integer sorted array
     *@param target :  an integer to be inserted
     *return : a list of length 2, [index1, index2]
     */
    public int[] searchRange(int[] A, int target) {
        // write your code here
        int[] ret = {-1, -1};
        int size = A.length;
        if (size == 0) {
            return ret;
        }

        //find index1
        int l = 0;
        int r = size - 1;
        int index1 = -1;

        if (A[0] == target) {
            index1 = 0;
        }
        else {
            if (A[size-1] == target) {
                index1 = size - 1;
            }
            while (r - l > 1) {
                int m = (l + r) / 2;
                if (A[m] < target)
                    l = m;
                else if(A[m] > target) {
                    r = m;
                }
                else { //A[m] == target
                    r = m;
                    index1 = m;
                }
            }
        }
        //find index2
        l = 0;
        r = size - 1;
        int index2 = -1;

        if (A[size-1] == target) {
            index2 = size - 1;
        }
        else {
            if (A[0] == target) {
                index2 = 0;
            }
            while (r - l > 1) {
                int m = (l + r) / 2;
                if (A[m] > target) {
                    r = m;
                }
                else if (A[m] < target) {
                    l = m;
                }
                else { //A[m] == target
                    l= m;
                    index2 = m;
                }
            }
        }
        ret[0] = index1;
        ret[1] = index2;
        return ret;
        
    }
}
