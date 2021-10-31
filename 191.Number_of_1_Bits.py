# https://leetcode.com/problems/number-of-1-bits/

def hammingweight(n):
    if n == 0: return 0
    hw = 0
    while n != 1:
        if n % 2 == 1:
            hw += 1
        n //= 2
    return hw + 1


if __name__ == '__main__':
    num = 0b00000000000000000000000000011011
    print(hammingweight(num))
