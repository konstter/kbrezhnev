# https://leetcode.com/problems/maximum-subarray/

def maxsubarray(nums):
    sum = 0
    max = nums[0]
    for i in range(len(nums)):
        sum += nums[i]
        if sum > max:
            max = sum
        if sum <= 0:
            sum = 0
    return max

n = [-5, -1, -3, -4]
print(maxsubarray(n))
