# https://leetcode.com/problems/contains-duplicate-ii/

def containsnearbyduplicate(nums, k):
    d = {}
    for i, val in enumerate(nums):
        if val in d:
            if abs(i - d[val]) <= k:
                return True
            else:
                d[val] = i
        else:
            d[val] = i
    return False


if __name__ == '__main__':
    # n = [1, 0, 1, 1]
    # kk = 1
    n = [1, 2, 3, 1, 2, 3]
    kk = 2
    print(containsnearbyduplicate(n, kk))