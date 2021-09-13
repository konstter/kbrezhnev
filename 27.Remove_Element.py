#https://leetcode.com/problems/remove-element/

def removeelement(nums, val):
    k = len(nums)
    i = 0
    while i < k:
        if nums[i] == val:
            nums.remove(val)
            k -= 1
        else:
            i += 1
    return k


v = 3
l = [3,2,2,3]

print(removeelement(l,v))