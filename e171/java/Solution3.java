import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Map;
import java.util.HashMap;
import java.util.Set;
import java.util.Map.Entry;

public class Solution3 {

	private static <K,V> boolean equals(Map<K,V> a, Map<K,V> b) {
		if (a.size() != b.size()) {
			return false;
		}
		for(K key:a.keySet()) {
			if (!a.get(key).equals(b.get(key)))
				return false;
		}
		return true;
	}

	private static Map<Character, Integer> toCharMap(String str) {
		Map<Character, Integer> map = new HashMap<Character, Integer>();
		Character key;
		for(int i=0;i < str.length(); i++) {
			key = str.charAt(i);
			if (map.containsKey(key)) {
				map.put(key, map.get(key)+1);
			}
			else {
				map.put(key, 1);
			}
		}
		return map;
	}
	/**
	 * @param strs: A list of strings
	 * @return: A list of strings
	 */
	public static List<String> anagrams(String[] strs) {
		List<Map<Character, Integer>> maps = new ArrayList<Map<Character, Integer>>(strs.length);
		for(int i=0; i < strs.length; i++) {
			maps.add(toCharMap(strs[i]));
		}


		List<String> returns = new ArrayList<String>();
		int[] flags = new int[strs.length];
		for(int i=0; i < strs.length; i++) {
			if (flags[i] == 1) {
				continue;
			}
			for(int j=i+1; j < strs.length; j++) {
				if (flags[j] == 1)
					continue;
				//if (maps.get(i).equals(maps.get(j))) {
				if (equals(maps.get(i),maps.get(j))) {
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
