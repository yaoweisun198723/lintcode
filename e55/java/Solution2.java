import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;

public class Solution2 {
    /**
    * @param A : A string includes Upper Case letters
    * @param B : A string includes Upper Case letter
    * @return :  if string A contains all of the characters in B return true else return false
     */
    public static boolean compareString(String A, String B) {
        // write your code here
		if (A.length() < B.length())
			return false;

		Map<Character, Integer> a_count = new HashMap<Character, Integer>();
		Map<Character, Integer> b_count = new HashMap<Character, Integer>();

		for (int i=0; i < A.length(); i++) {
			//count every char of string s
			Character tmp_k = new Character(A.charAt(i));
			Integer tmp_v = a_count.get(tmp_k);
			if (tmp_v == null) {
				a_count.put(tmp_k, 1);
			} else {
				a_count.put(tmp_k, tmp_v+1);
			}
		}

		for (int i=0; i < B.length(); i++) {
			//count every char of string t
			Character tmpKey = new Character(B.charAt(i));
			Integer tmpV = b_count.get(tmpKey);
			if (tmpV == null) {
				b_count.put(tmpKey, 1);
			} else {
				b_count.put(tmpKey, tmpV+1);
			}
		}

		boolean result = true;
		for (Entry<Character, Integer> entry : b_count.entrySet()) {
			if (a_count.get(entry.getKey()) < entry.getValue()) {
				result = false;
				break;
			}
		}
		return result;
    }

	public static void main(String[] args) {
		boolean result = compareString(args[0], args[1]);
		System.out.println(result);
	}
};
