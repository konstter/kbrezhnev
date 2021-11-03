# https://leetcode.com/problems/reverse-bits/

def reversebits(n):
    '''
    The function scans a input parameter bit by bit from the end.
    It assigns "1" with shift to the left by (31 - "shift") positions
    if the parameter is an odd number. After that, "Res" gets
    sum itself with the shifted value.
    But If the parameter is an even number the function shifts it
    to the right by one position with "0" until it becomes zero.
    '''
    res = 0
    shift = 0
    while n:
        if n & 1:
            res |= 1 << (32 - shift - 1)
        shift += 1
        n >>= 1
    return res

if __name__ == '__main__':
    n = 0b00000010100101000001111010011100
    print(reversebits(n))


