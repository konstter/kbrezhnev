
# https://leetcode.com/problems/palindrome-number/

def ispalindrome(x):
    '''
    :param x: Integer
    :return: True or False
    '''
    if x < 0:
        return False
    if x > 0 and x % 10 == 0:
        return False
    y = 0
    x_cache = x
    while x_cache:
        y = y*10 + x_cache % 10
        x_cache //= 10
    return x == y

num = 101
print(ispalindrome(num))
    #     y = 0.1
    #     x_cache = x
    #     while x != 0:
    #         x //= 10
    #         y *= 10
    #     while y >= 10:
    #         if x_cache % 10 == x_cache // y:
    #             x_cache %= y
    #             print(x_cache)
    #             x_cache //= 10
    #             print(x_cache)
    #             y /= 100
    #         else:
    #             return False
    #     return True
    # else:
    #     return False

