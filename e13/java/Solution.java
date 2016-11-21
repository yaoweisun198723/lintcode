class Solution {
    /**
     * Returns a index to the first occurrence of target in source,
     * or -1  if target is not part of source.
     * @param source string to be scanned.
     * @param target string containing the sequence of characters to match.
     */
    public static int strStr(String source, String target) {
        //write your code here
		if (source == null || target == null)
			return -1;
		int lenSrc=source.length();
		int lenTgt=target.length();

		if (lenTgt == 0)
			return 0;
		if (lenSrc < lenTgt)
			return -1;

		int equalLen = 0;
		int index = 0;
		for(int i = 0; i <= lenSrc - lenTgt; i++) {
			index = i;
			equalLen = 0;
			for (int j=0; j < lenTgt; j++) {
				if (source.charAt(i+j) == target.charAt(j)) {
					equalLen++;
				}
			}
			if (equalLen == lenTgt) {
				break;
			}
		}
		if (equalLen == lenTgt)
			return index;
		else
			return -1;
    }

	public static void main(String[] args) {
		int result = strStr(args[0], args[1]);
		System.out.println(result);
		System.out.println(strStr(null, "a"));
	}
}
