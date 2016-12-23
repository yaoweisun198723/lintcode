import java.util.Arrays;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

public class Solution {
    /**
     * @param numbers : Give an array numbersbers of n integer
     * @param target : you need to find four elements that's sum of target
     * @return : Find all unique quadruplets in the array which gives the sum of
     *           zero.
     */
    public ArrayList<ArrayList<Integer>> fourSum(int[] numbers, int target) {
        /* your code */
        int size = numbers.length;
        Map<ArrayList<Integer>, Integer> result = new HashMap<ArrayList<Integer>, Integer>();
        Arrays.sort(numbers);
        for (int first=0; first < size-3; first++) {
            for (int second=first+1; second<size-2; second++) {
                int third = second + 1;
                int fourth = size - 1;
                while (third < fourth) {
                    int sum = numbers[first] + numbers[second] +
                              numbers[third] + numbers[fourth];
                    if (sum > target) {
                        fourth--;
                    }
                    else if (sum < target) {
                        third++;
                    }
                    else { //sum == target
                        Integer[] quadruplets = {numbers[first], numbers[second], numbers[third], numbers[fourth]};
                        ArrayList<Integer> found = 
                                    new ArrayList<Integer>(Arrays.asList(quadruplets));
                        result.put(found, 1);
                        third++;
                        fourth--;
                    }
                }
            }
        }
        return new ArrayList<ArrayList<Integer>>(result.keySet());
    }
}
