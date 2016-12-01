import java.util.ArrayList;

public class Solution {
    /**
     * @param nums: A list of integers
     * @return: A list of integers includes the index of the first number 
     *          and the index of the last number
     */
    public ArrayList<Integer> subarraySum(int[] nums) {
        // write your code here
		ArrayList<Integer> ret = new ArrayList<Integer>();
		for (int first=0; first < nums.length; first++) {
			int subsum = nums[first];
			if (subsum == 0) {
				ret.add(first);
				ret.add(first);
				return ret;
			}
			for (int subLen=2; first+subLen-1 < nums.length; subLen++) {
				subsum += nums[first+subLen-1];
				if (subsum == 0) {
					ret.add(first);
					ret.add(first + subLen - 1);
					return ret;
				}
			}
		}
		return ret;
    }

	public static void main(String[] args) {
		new Solution().subarraySum();
	}
}
