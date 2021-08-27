
# https://leetcode.com/problems/palindrome-number/

def ispalindrome(x):
    '''
    :param x: Integer
    :return: True or False
    '''
    if 0 <= x < pow(2, 31) - 1:
        y = 0.1
        x_cache = x
        while x != 0:
            x //= 10
            y *= 10
        print(int(y))
        print(x_cache)
        while y >= 10:
            print(x_cache % 10)
            print(x_cache // y)
            if x_cache % 10 == int(x_cache // y):
                x_cache %= y
                print(x_cache)
                x_cache //= 10
                print(x_cache)
                y /= 100
            else:
                return False
        return True
    else:
        return False

num = 0
print(ispalindrome(num))