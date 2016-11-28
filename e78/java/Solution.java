public class Solution {
    /**
     * @param strs: A list of string
     * @return: The longest common prefix
     */
    public String longestCommonPrefix(String[] strs) {
        // write your code here
		if (strs == null || strs.length == 0) {return "";}

		int minLen = strs[0].length();
		for (int i=1; i < strs.length; i++) {
			minLen = minLen <= strs[i].length() ? minLen : strs[i].length();
		}

		StringBuilder ret = new StringBuilder();
		for (int i=0; i < minLen; i++) {
			char tmp = strs[0].charAt(i);
			boolean same = true;
			for (int j=1; j < strs.length; j++) {
				if (strs[j].charAt(i) != tmp) {
					same = false;
				}
			}
			if (same == false) {
				return ret.toString();
			}
			else {
				ret.append(tmp);
			}
		}
		return ret.toString();
    }

	public static void main(String[] args) {
		String lcp = new Solution().longestCommonPrefix(args);
		System.out.println(lcp);
		String[] strs = {};
		String lcp2 = new Solution().longestCommonPrefix(strs);
		strs = null;
		lcp2 = new Solution().longestCommonPrefix(strs);
		System.out.println(lcp2);
	}
}
