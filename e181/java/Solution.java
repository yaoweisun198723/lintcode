class Solution {
    /**
     *@param a, b: Two integer
     *return: An integer
     */
    public static int bitSwapRequired(int a, int b) {
        // write your code here
        int xor = a ^ b;
        int count = 0;
        int shift = 1;
        for (int i=0; i<32; i++) {
            //System.out.print(i);
            if ((xor & (shift << i)) != 0) {
                count++;
            }
        }

        return count;
    }
};
