public class Solution {
    /**
     *@param A: A positive integer which has N digits, A is a string.
     *@param k: Remove k digits.
     *@return: A string
     */
    public String DeleteDigits(String A, int k) {
        // write your code here
        StringBuilder stb = new StringBuilder();
        int lastIdx = -1;
        for (int i =0; i<A.length()-k; i++) {
            int min = 10;
            for (int j=lastIdx+1; j<=i+k; j++) {
                int tmp = A.charAt(j) - '0';
                if (tmp < min) {
                    min = tmp;
                    lastIdx = j;
                    
                }
            }
            stb.append(Integer.toString(min));
        }
        String ret = stb.toString();
        for (int l=0; l<ret.length(); l++) {
            if (ret.charAt(l) != '0') {
                ret = ret.substring(l);
                break;
            }
        }
        return ret;
        
    }
}
