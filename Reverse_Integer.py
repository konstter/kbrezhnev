
def reverse(x):
    '''
    :param x: Integer
    :return:
    '''
    if x == 0:
        return 0
    else:
        int_max = pow(2, 31)-1
        int_min = pow(-2, 31)
        y = 0
        tmp = abs(x)
        while tmp != 0:
            pop = tmp % 10
            tmp //= 10
            if y > int_max/10 or (y == int_max/10 and pop > 7):
                return 0
            # if y < int_min/10 or (y == int_min/10 and pop < -8):
            #     return 0
            y = y * 10 + pop
        if x < 0:
            return y * -1
        else:
            return y

num = 71
print(reverse(num))
