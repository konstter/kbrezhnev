# https://leetcode.com/problems/number-of-1-bits/

def hammingweight(n):
    if n == 0: return 0
    hw = 0
    while n:
        if n & 1:
            hw += 1
        n >>= 1
    return hw


if __name__ == '__main__':
    num = 0b00000000000000000000000000011011
    print(hammingweight(num))
