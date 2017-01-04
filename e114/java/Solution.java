import java.math.BigInteger;
public class Solution {
    /**
     * @param n, m: positive integer (1 <= n ,m <= 100)
     * @return an integer
     */
    public int uniquePaths(int m, int n) {
        // write your code here 
        int more = m > n?m:n;
        int less = m < n?m:n;
        
        BigInteger ret = new BigInteger("1");
        for (Integer i=more; i<=less+more-2; i++) {
            ret = ret.multiply(new BigInteger(i.toString()));
        }
        for (Integer j=1; j<=less-1; j++) {
            ret = ret.divide(new BigInteger(j.toString()));
        }
        return ret.intValue();
    }
}
