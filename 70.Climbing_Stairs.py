# https://leetcode.com/problems/climbing-stairs/


def climbstairs(n):
    f = [0, 1]
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
        print(f)
    return f[n - 1] + f[n]

print(climbstairs(2))
