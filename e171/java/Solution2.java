import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Map;
import java.util.HashMap;
import java.util.Set;
import java.util.Map.Entry;

public class Solution2 {

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

	/**
	 * @param strs: A list of strings
	 * @return: A list of strings
	 */
	public static List<String> anagrams(String[] strs) {
		List<String> returns = new ArrayList<String>();
		int[] flags = new int[strs.length];
		for(int i=0; i < strs.length; i++) {
			if (flags[i] == 1) {
				continue;
			}
			for(int j=i+1; j < strs.length; j++) {
				if (flags[j] == 1)
					continue;
				if (anagram(strs[i], strs[j])) {
					flags[j] = 1;
					flags[i] = 1;
				}
			}
		}
		for(int i=0; i < strs.length; i++) {
			if (flags[i] == 1) {
				returns.add(strs[i]);
			}
		}
		return returns;
	}

	public static void main(String[] args) {
		String[] strs = {"lint", "intl", "inlt", "code"};
		for(String str:anagrams(strs)) {
			System.out.print(str + '\t');
		}
		System.out.println();
		if (args.length >= 2) {
			for(String str:anagrams(args)) {
				System.out.print(str + '\t');
			}
		}
	}
}
