# https://leetcode.com/problems/reverse-bits/

def reversebits(n):
    res = 0
    for i in range(32):
        bit = n % 2
        n >>= 1
        res = res | bit << (31-i)
    return res


if __name__ == '__main__':
    n = 0b00000010100101000001111010011100
    print(reversebits(n))

