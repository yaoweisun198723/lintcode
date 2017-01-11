public class Solution {
    /**
     * @param nums: a list of integers
     * @return: find a  majority number
     */
    public int majorityNumber(ArrayList<Integer> nums) {
        // write your code
        // ref:http://blog.csdn.net/gukesdo/article/details/7585636
        int count = 0;
        int major = 0;
        for (Integer num:nums) {
            if (count == 0) {
                major = num;
                count = 1;
            }
            else {
                if (major == num) {
                    count++;
                }
                else {
                    count--;
                }
            }
            
        }
        return major;
    }
}
