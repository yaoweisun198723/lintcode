import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Map;
import java.util.HashMap;
import java.util.Set;
import java.util.Map.Entry;
public class Solution {
    /**
     * @param A, B: Two string.
     * @return: the length of the longest common substring.
     */
    public static int longestCommonSubstring(String A, String B) {
        // write your code here
		String longer;
		String shorter;
		if (A.length() > B.length()) {
			longer = A;
			shorter = B;
		}
		else {
			longer = B;
			shorter = A;
		}
		for(int max_len=shorter.length(); max_len > 0; max_len--) {
			for(int i=0; i + max_len -1 < shorter.length(); i++) {
				String tmp = shorter.substring(i, i+max_len);
				//System.out.println("shorter:" + tmp);
				for(int j=0; j + max_len -1 < longer.length(); j++) {
					//System.out.println("longer:" + longer.substring(j, j+max_len));
					if (tmp.equals(longer.substring(j, j+max_len)))
						return max_len;
				}
			}
		}
		return 0;
    }

	public static void main(String[] args) {
		System.out.println(longestCommonSubstring("abcdefg", "def"));
		if (args.length >= 2) {
			System.out.println(longestCommonSubstring(args[0], args[1]));
		}
	}
}
