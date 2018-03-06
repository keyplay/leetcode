        if x < 0:
            return False
        """x_str = str(x)
        return x_str == x_str[::-1]"""
    
        ranger = 1
        while x / ranger >= 10:
            ranger *= 10

        while x:
            left = x / ranger
            right = x % 10
            if left != right:
                return False
            
            x = (x % ranger) / 10
            ranger /= 100

        return True
