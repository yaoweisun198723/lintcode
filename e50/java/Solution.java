import java.util.ArrayList;
public class Solution {
    /**
     * @param A: Given an integers array A
     * @return: A Long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
     */
    public static ArrayList<Long> productExcludeItSelf(ArrayList<Integer> A) {
        // write your code
        ArrayList<Long> ret = new ArrayList<Long>(A.size());
        for (int i=0; i < A.size(); i++) {
            Long product = 1L;
            for (int j=0; j < A.size(); j++) {
                if (j != i) {
                    product *= A.get(j);
                }
            }
            ret.add(product);
        }
        return ret;
    }
	public static void main(String[] args) {
		int length = 21;
		if (args.length > 0) {
			length = Integer.valueOf(args[0]);
		}
		ArrayList<Integer> input =  new ArrayList<Integer>(Integer.valueOf(length));
		for (int i=0; i < length; i++) {
			input.add(1);
		}
		ArrayList<Long> product = productExcludeItSelf(input);
		for (int i=0; i < length; i++) {
			System.out.print(product.get(i).toString() + ' ');
		}
	}
}
