public class Solution {

    /**
     *@param n: Given a decimal number that is passed in as a string
     *@return: A string
     */
    String binaryRepresentation(String n) {
        // wirte your code here
		//System.out.println(n.split(".").length);
        int integer = Integer.valueOf(n.split("\\.")[0]);
        System.out.println(integer);
        double fraction = Double.valueOf("."+n.split("\\.")[1]);
        System.out.println(fraction);

        // Integer part
        String int_str = "";
        while (integer > 0) {
            int_str =  integer % 2 + int_str;
            integer /= 2;
        }
        if (int_str == "") {
            int_str = "0";
        }


        // Fraction part
        String frac_str = "";
        System.out.println(fraction);
        if (fraction != 0.0) {
            int frac_len = n.length() - n.indexOf('.') - 1;
            while (fraction != 0.0) {
				if (frac_str.length() > 32)
					break;
                fraction *= 2;
				int tmp = (int)Math.floor(fraction);
                frac_str = frac_str + tmp;
                fraction = fraction - tmp;
            }
        }
        
        
        if (fraction != 0.0) {
            return "ERROR";
        }
        else {
            if (frac_str == "") {
                return int_str;
            }
            else {
                return int_str + "." + frac_str;
            }
        }
    }

	public static void main(String[] args) {
		String s = new Solution().binaryRepresentation(args[0]);
		System.out.println(s);
	}
};
