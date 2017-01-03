class Solution {
    /*
     * @param n: An integer
     * @return: True or false
     */
    public boolean checkPowerOf2(int n) {
        // write your code here
        if (n < 1) {
            return false;
        }
        if (n == 1) {
            return true;
        }
        while (n > 1) {
            int mod = n %2;
            if (mod == 1) {
                return false;
            }
            n = n / 2;
        }
        return true;
    }
};
