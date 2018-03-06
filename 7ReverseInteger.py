class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
     
        flag = 1 if x > 0 else -1
        x_str = str(x * flag)
        x_output = int(x_str[::-1])
        return x_output * flag if x_output / 0x7FFFFFFF < 1 else 0
