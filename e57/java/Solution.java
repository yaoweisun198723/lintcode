import java.util.Arrays;

public class Solution {
    /**
     * @param numbers : Give an array numbers of n integer
     * @return : Find all unique triplets in the array which gives the sum of zero.
     */
    public ArrayList<ArrayList<Integer>> threeSum(int[] numbers) {
        // write your code here
        Arrays.sort(numbers);
        int size = numbers.length;
        ArrayList<ArrayList<Integer>> result = 
                new ArrayList<ArrayList<Integer>>();
        ArrayList<Integer> last = null;
        for (int i=0; i<size-2; i++) {
            if ((i == 0) || (i >= 1) && (numbers[i] != numbers[i-1])) {
                int left = i+1;
                int right = size-1;
                while (left < right) {
                    int tmp = numbers[i] + numbers[left] + numbers[right];
                    if (tmp == 0) {
                        ArrayList<Integer> a = new ArrayList<Integer>(3);
                        a.add(numbers[i]);
                        a.add(numbers[left]);
                        a.add(numbers[right]);
                        if (!a.equals(last)) {
                            result.add(a);
                            last = a;
                        }
                        left++;
                        right--;
                    }
                    else if (tmp > 0) {
                        right--;
                    }
                    else {  //tmp < 0
                        left++;
                    }
                }
            }
        }
        return result;
        
    }
}
