
def reverse(x):
    '''
    :param x: Integer
    :return:
    '''
    if x != 0:
        int_max = pow(2, 31)-1
        int_min = pow(-2, 31)
        y = 0
        while x != 0:
            pop = abs(x) % 10
            x //= 10
            # if y > int_max/10 or (y == int_max/10 and pop > 7):
            #     return 0
            # if y < int_min/10 or (y == int_min/10 and pop < -8):
            #     return 0
            y = y * 10 + pop
        return y
    else:
        return 0


num = -7
print(num % 5)
# print(reverse(num))
