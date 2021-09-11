# https://leetcode.com/problems/sqrtx/

def mysqrt(x):
    if not x or x == 1: return x
    l, r = 0, x
    while l < r:
        mid = (l + r) // 2
        if mid ** 2 <= x < (mid + 1) ** 2:
            return mid
        if mid ** 2 > x:
            r = mid
        else:
            l = mid + 1
    return l


print(mysqrt(1024))

