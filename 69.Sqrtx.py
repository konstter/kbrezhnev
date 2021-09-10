# https://leetcode.com/problems/sqrtx/

def mysqrt(x):
    y = 0
    while y * y < x:
        y += 10
    while y * y > x:
        y -= 1
    if y * y <= x:
        return y
    else:
        return y - 1


given = 1024
print(mysqrt(given))
