
# https://leetcode.com/problems/single-number/

def singlenumber(nums):
    l = len(nums)
    if l == 1: return nums[0]
    nums.sort()
    i = 0
    while i < l - 1:
        if nums[i] != nums[i+1]:
            return nums[i]
        i += 2
    return nums[-1]


if __name__ == '__main__':
    print(singlenumber([3, 2, 5, 2, 5]))
