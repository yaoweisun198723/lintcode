import java.util.ArrayList;
import java.util.Comparator;
public class Solution {
    class Sum {
        public final int value;
        public final int index;
        public Sum(int x, int y) {
            this.value = x;
            this.index = y;
        }
    }
    class SumComparator implements Comparator<Sum> {
        @Override
        public int compare(Sum s1, Sum s2) {
            return s1.value - s2.value;
        }
    }
    /**
     * @param nums: A list of integers
     * @return: A list of integers includes the index of the first number 
     *          and the index of the last number
     */
    public int[] subarraySumClosest(int[] nums) {
        // write your code here
        ArrayList<Sum> sums = new ArrayList<Sum>();
        Sum zero = new Sum(0, -1);
        sums.add(zero);
        int tmp = 0;
        for (int i=0; i<nums.length; i++)
        {
            tmp += nums[i];
            Sum sum = new Sum(tmp, i);
            sums.add(sum);
        }
        sums.sort(new SumComparator());
        int diff = Integer.MAX_VALUE;
        int start = 0;
        int end = 0;
        for (int j=1; j<sums.size(); j++) 
        {
            if (Math.abs(sums.get(j).value - sums.get(j-1).value) < diff)
            {
                start = Math.min(sums.get(j).index, sums.get(j-1).index) + 1;
                end = Math.max(sums.get(j).index, sums.get(j-1).index);
                diff = Math.abs(sums.get(j).value - sums.get(j-1).value);
            }
        }
        int[] ret = {start, end};
        return ret;
    }
}
