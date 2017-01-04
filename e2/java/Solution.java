class Solution {
    /*
     * param n: As desciption
     * return: An integer, denote the number of trailing zeros in n!
     */
    public long trailingZeros(long n) {
        // write your code here
        long zeros = 0L;
        long radix = 5L;
        while(true) {
            long tmp = n / radix;
            if (tmp == 0) {
                break;
            }
            zeros += tmp;
            radix *= 5L;
        }
        return zeros;
    }
};
