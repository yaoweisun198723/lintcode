import java.util.Arrays;

public class Solution {
    /**
     * @param numbers: Give an array numbers of n integer
     * @param target : An integer
     * @return : return the sum of the three integers, the sum closest target.
     */
    public int threeSumClosest(int[] numbers, int target) {
        // write your code here
        Arrays.sort(numbers);
        int size = numbers.length;
        int sum = numbers[0] + numbers[1] + numbers[2];
        int left, right;
        for (int i=0; i<size-2; i++) {
            left = i+1;
            right = size - 1;
            while (left < right) {
                int tmp = numbers[i]+numbers[left]+numbers[right];
                if (Math.abs(tmp-target) < Math.abs(sum-target)) {
                    sum = tmp;
                }
                if (tmp > target) {
                    right--;
                }
                else {
                    left++;
                }
            }
        }
        return sum;
    }
}
