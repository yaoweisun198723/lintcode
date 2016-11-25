import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Map;
import java.util.HashMap;
import java.util.Set;
import java.util.Map.Entry;

public class Solution {

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
		Map<String, List<String>> anaMap = new HashMap<String, List<String>>();
		for(String str:strs) {
			Boolean found = false;
			for(String key:anaMap.keySet()) {
				if (anagram(str, key)) {
					anaMap.get(key).add(str);
					found = true;
					break;
				}
			}
			if (found == false) {
				List<String> tmp = new ArrayList<String>();
				tmp.add(str);
				anaMap.put(str, tmp);
			}
		}

		List<String> returns = new ArrayList<String>();
		for(List<String> anagram:anaMap.values()) {
			if (anagram.size() > 1) {
				returns.addAll(anagram);
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
