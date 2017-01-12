import java.util.Arrays;
public class Solution {
    class ConcatComparator implements java.util.Comparator<Integer> {
        public int compare(Integer x, Integer y) {
            int equal = 0;
            char[] charx = x.toString().toCharArray();
            char[] chary = y.toString().toCharArray();
            int xlen = charx.length;
            int ylen = chary.length;
            int minlen = xlen < ylen?xlen:ylen;
            for (int i=0; i<minlen; i++) {
                if (charx[i] < chary[i]) {
                    equal = 1;
                    break;
                }
                else if (charx[i] > chary[i]) {
                    equal = -1;
                    break;
                }
                else {
                    equal = 0;
                }
            }
            if (equal == 0 && xlen != ylen) {
                if (xlen > ylen) {
                    if (charx[minlen] > charx[0]) {
                        equal = -1;
                    }
                    else if(charx[minlen] < charx[0]) {
                        equal = 1;
                    }
                    else {
                        equal = 0;
                    }
                }
                else if(xlen < ylen) {
                    if (chary[minlen] > chary[0]) {
                        equal = 1;
                    }
                    else if(chary[minlen] < chary[0]) {
                        equal = -1;
                    }
                    else {
                        equal = 0;
                    }
                }
                else {
                    equal = 0;
                }
            }
            return equal;

        }
    }
    
    /**
     *@param num: A list of non negative integers
     *@return: A string
     */
    public String largestNumber(int[] num) {
        // write your code here
		Integer[] nums = new Integer[num.length];
		for (int i=0; i<num.length; i++) {
		    nums[i] = num[i];
		}
        Arrays.sort(nums, new Solution.ConcatComparator());
        StringBuilder str = new StringBuilder();
        for (int e:nums) {
            str.append(e);
        }
        String ret = str.toString();
        if (ret.charAt(0) == '0')
            ret = "0";
        return ret;
    }
}
