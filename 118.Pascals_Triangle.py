# https://leetcode.com/problems/pascals-triangle/

def generate(numrows):
    if numrows == 1: return [[1]]
    triangle = [[1]]
    nr = 1
    while nr <= numrows - 1:
        tmp = [1] * (nr + 1)
        for i in range(nr + 1):
            if i != 0 and i != nr:
                tmp[i] = triangle[nr-1][i-1] + triangle[nr-1][i]

        triangle.append(tmp)
        nr += 1
    return triangle


print(generate(5))
