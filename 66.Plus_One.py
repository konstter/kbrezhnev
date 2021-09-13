# https://leetcode.com/problems/plus-one/

def plusone(digits):
    digits[-1] += 1
    l, i = len(digits), -1
    while digits[i] == 10:
        digits[i] = 0
        if i != l * -1:
            digits[i - 1] += 1
            i -= 1
        else:
            digits.insert(0, 1)
    return digits


d = [9]
print(plusone(d))
