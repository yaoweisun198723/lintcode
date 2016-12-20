import java.util.ArrayList;
public class Solution {
    /**
     * @param str: A string
     * @return An integer
     */
    public int atoi(String str) {
        // write your code here
		if (str == null || str == "") {
			return 0;
		}
		int sign;
		int begin;
		char[] chars = str.trim().toCharArray();
		if (chars[0] == '-') {
			sign = -1;
			begin = 1;
		}
		else if (chars[0] == '+') {
			sign = 1;
			begin = 1;
		}
		else {
			sign = 1;
			begin = 0;
		}
		ArrayList<Integer> ints = new ArrayList<Integer>();
		for(int i=begin; i < chars.length; i++) {
			if (chars[i] >= '0' && chars[i] <= '9') {
				ints.add((int)(chars[i]-'0'));
			}
			else {
				break;
			}
		}
		long result = 0;
		for (int j=0; j<ints.size(); j++) {
			result += ints.get(j) * (Math.pow(10,(ints.size()-1-j)));
		}
		if (result > 2147483647 && sign == 1)
			return 2147483647;
		else if (result > 2147483648L && sign ==  -1)
			return -2147483648;
		else
			return (int)result * sign;
    }
	public static void main(String[] args) {
		System.out.println(new Solution().atoi("  -1234562"));
		System.out.println(new Solution().atoi("145.62"));
		System.out.println(new Solution().atoi(args[0]));
	}
}
