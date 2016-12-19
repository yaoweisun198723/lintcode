public class Solution {
	/** 
     *@param nums: The integer array you should partition
     *@param k: As description
     *return: The index after partition
     */
    public int partitionArray(int[] nums, int k) {
	    //write your code here
	    if (nums.length == 0)
	        return 0;
	    int lp = 0;
	    int rp = nums.length - 1;
	    while(lp < rp) {
	        if (nums[lp] < k) {
	            lp++;
	            continue;
	        }
	        if (nums[rp] >= k) {
	            rp--;
	            continue;
	        }
	        //swap two elements
	        int tmp = nums[lp];
	        nums[lp] = nums[rp];
	        nums[rp] = tmp;
	        lp++;
	        rp--;
	    }
	    if (nums[lp] >= k) {
	        return lp;
	    }
	    else {
	        return lp+1;
	    }
    }
}
