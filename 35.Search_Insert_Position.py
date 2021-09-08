# https://leetcode.com/problems/search-insert-position/

def searchinsert(nums, target):
    for i, item in enumerate(nums):
        if target <= item:
            return i
    return i + 1


n = [1, 3, 5, 6]
t = 5
print(searchinsert(n, t))
