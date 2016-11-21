import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;

public class Solution2 {
    /**
     * @param s: The first string
     * @param b: The second string
     * @return true or false
     */
    public static boolean anagram(String s, String t) {
        // write your code here
		if (s.length() != t.length())
			return false;

		Map<Character, Integer> s_count = new HashMap<Character, Integer>();
		Map<Character, Integer> t_count = new HashMap<Character, Integer>();

		int len = s.length();
		for (int i=0; i < len; i++) {
			//count every char of string s
			Character tmp_k = new Character(s.charAt(i));
			Integer tmp_v = s_count.get(tmp_k);
			if (tmp_v == null) {
				s_count.put(tmp_k, 1);
			} else {
				s_count.put(tmp_k, tmp_v+1);
			}

			//count every char of string t
			Character tmpKey = new Character(t.charAt(i));
			Integer tmpV = t_count.get(tmpKey);
			if (tmpV == null) {
				t_count.put(tmpKey, 1);
			} else {
				t_count.put(tmpKey, tmpV+1);
			}
		}

		boolean result = true;
		for (Entry<Character, Integer> entry : s_count.entrySet()) {
			if (t_count.get(entry.getKey()) != entry.getValue()) {
				result = false;
				break;
			}
		}
		return result;
    }

	public static void main(String[] args) {
		boolean result = anagram(args[0], args[1]);
		System.out.println(result);
	}
};
