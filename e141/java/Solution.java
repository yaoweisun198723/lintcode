class Solution {
    /**
     * @param x: An integer
     * @return: The sqrt of x
     */
    public int sqrt(int x) {
        // write your code here
        long left = 1;
        long right = (long)x;
		long lx = (long)x;
        while (left <= right) {
            if (left * left <= lx && (left+1) * (left+1) > lx) {
                return (int)left;
            }
            long mid = (left + right) / 2;
            if (mid * mid < lx) {
                left  = mid;
            }
            else if (mid * mid > lx) {
                right = mid;
            }
            else {
                return (int)mid;
            }
        }
        return 0;
    }

	public static void main(String[] args) {
		System.out.println(new Solution().sqrt(Integer.valueOf(args[0])));
	}

}

