
# https://leetcode.com/problems/palindrome-number/

def ispalindrome(x):
    '''
    :param x: Integer
    :return: True or False
    '''
    if x >= 0:
        int_max = pow(2, 31)-1
        y = 0
        x_cache = x
        while x != 0:
            pop = abs(x) % 10
            x //= 10
            if y > int_max/10 or (y == int_max/10 and pop > 7):
                return False
            y = y * 10 + pop
        if x_cache == y:
            return True
        else:
            return False
    else:
        return False


num = 0
print(ispalindrome(num))