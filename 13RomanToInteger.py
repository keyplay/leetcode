class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum_out = 0
        num_dict = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        """
        i = 0
        while i < len(s):
            if i == len(s) - 1:
                sum_out += num_dict[s[i]]
                break
                    
            if num_dict[s[i]] >= num_dict[s[i+1]]:
                sum_out += num_dict[s[i]]
                i += 1
            else:
                sum_out += (num_dict[s[i+1]] - num_dict[s[i]])
                i += 2
                
            print i, sum_out
            
        return sum_out"""
    
        z = 0
        for i in range(0, len(s) - 1):
            if num_dict[s[i]] < num_dict[s[i+1]]:
                z -= num_dict[s[i]]
            else:
                z += num_dict[s[i]]
        return z + num_dict[s[-1]]
