class Solution {
    /*
     * @param a, b, n: 32bit integers
     * @return: An integer
     */
    public int fastPower(int a, int b, int n) {
        // write your code here
        if (n == 0) {
            return 1 % b;
        }
        if (a == 0) {
            return 0;
        }
        long longA = a;
        long longB = b;
        long extra = 1;
        while (n > 0) {
            if (n % 2 == 1) {
                extra = (extra * longA) % longB;
            }
            longA = (longA * longA) % longB;
            
            //System.out.println(a);

            n = n / 2;
        }
        return (int)extra;
    }
};
