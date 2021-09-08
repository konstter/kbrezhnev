
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
#

def removeduplicates(nums):
    if not nums:
        return 0
    i, l = 0, len(nums)
    for j in range(1, l):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    print(nums)
    return i + 1


n = [1, 1, 1, 2]
print(removeduplicates(n))

