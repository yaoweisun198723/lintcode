class Solution {
    /**
     *@param n, m: Two integer
     *@param i, j: Two bit positions
     *return: An integer
     */
    public int updateBits(int n, int m, int i, int j) {
        // write your code here
        int a = j+1 >= 32?0:1 << (j+1);
        int tmp = n & ( a - (1 << i) );

        return n - tmp + (m << i);
        
    }
}
