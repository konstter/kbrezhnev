# https://leetcode.com/problems/pascals-triangle-ii/

def getrow(rowindex: int):
    if rowindex == 0: return [1]
    nr = 1
    while nr <= rowindex:
        tmp = [1] * (nr + 1)
        for i in range(nr + 1):
            if i != 0 and i != nr:
                tmp[i] = triangle[i-1] + triangle[i]
        nr += 1
        triangle = tmp
    return triangle


print(getrow(4))
