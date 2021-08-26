
def reverse(x):
    '''
    :param x: Integer
    :return:
    '''
    if pow(-2, 31) < x < pow(2, 31)-1 and x != 0:
        f_string = str(abs(x))
        r_string = f_string[::-1]
        if r_string[0] == '0':
            r_string = r_string[1:]
        if x < 0:
            return int(r_string)*-1
        else:
            return int(r_string)
    else:
        return 0


num = -1230

print(reverse(num))
