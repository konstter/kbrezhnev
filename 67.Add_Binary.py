# https://leetcode.com/problems/add-binary/

def bintodec(k):
    x = 0
    res = 0
    for i in range(len(k)-1, -1, -1):
        res += 2 ** x * int(k[i])
        x += 1
    return res


def dectobin(n):
    res = ""
    while n != 0:
        r = n % 2
        print(n, r)
        res = str(r) + res
        n = n // 2
    return res


def addbinary(a, b):
    if a == '0': return b
    if b == '0': return a
    n = bintodec(a) + bintodec(b)
    return dectobin(n)


astr = "1010"
bstr = "1011"
print(addbinary(astr, bstr))

