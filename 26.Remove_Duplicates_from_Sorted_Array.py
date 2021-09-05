# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

def removeduplicates(nums):
    i = 0
    l = len(nums)
    while i <= l-2:
        if nums[i] != nums[i+1]:
            i += 1
        else:
            nums.remove(nums[i])
            l -= 1
    return l


n = [1, 1, 2]
print(removeduplicates(n))
