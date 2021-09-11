# https://leetcode.com/problems/add-binary/

def addbinary(a: str, b: str) -> str:
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    res = ''
    c = 0
    for i in range(max_len - 1, -1, -1):
        r = c
        r += 1 if a[i] == '1' else 0
        r += 1 if b[i] == '1' else 0
        res = ('1' if r % 2 == 1 else '0') + res
        c = 0 if r < 2 else 1
    if c != 0: res = '1' + res
    return res


print(addbinary('1101', '100'))


