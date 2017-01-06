class Solution:
    #@param n: Given a decimal number that is passed in as a string
    #@return: A string
    def binaryRepresentation(self, n):
        # write you code here
        fraction = float(n) % 1
        integer = int(float(n) - fraction)

        # Integer part
        int_str = ''
        while integer > 0:
            int_str = str(integer % 2) + int_str
            integer /= 2
        if int_str == '':
            int_str = '0'
        #print int_str

        # Fraction part
        frac_str = ''
        if fraction != 0:
            frac_len = len(n) - n.find('.') - 1
            for i in range(frac_len):
                fraction *= 2
                frac_str = frac_str + str(int(fraction // 1))
                fraction = fraction % 1
        
        
        if fraction != 0:
            return 'ERROR'
        else:
            if frac_str == '':
                return int_str
            else:
                return int_str + '.' + frac_str
