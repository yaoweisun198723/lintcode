import java.util.Arrays;

public class Solution1 {
    /**
     * @param s: The first string
     * @param b: The second string
     * @return true or false
     */
    public static boolean anagram(String s, String t) {
        // write your code here
		char[] cs = s.toCharArray();
		char[] ct = t.toCharArray();
		Arrays.sort(cs);
		Arrays.sort(ct);
		if (cs.length != ct.length) {
			return false;
		} else {
			boolean result=true;
			for (int i=0; i < cs.length; i++) {
				if (cs[i] != ct[i])
					result=false;
			}
			return result;
		}
    }

	public static void main(String[] args) {
		boolean result = anagram(args[0], args[1]);
		System.out.println(result);
	}
};
