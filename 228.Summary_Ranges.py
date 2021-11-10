# https://leetcode.com/problems/summary-ranges/

def summaryranges(nums):
    if not nums: return None
    res, j = [], nums[0]
    nums.append(nums[-1])
    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] > 1 or nums[i] == nums[i-1]:
            if nums[i-1] == j:
                res.append(str(j))
            else:
                res.append(str(j)+'->'+str(nums[i-1]))
            j = nums[i]
    return res


if __name__ == '__main__':
    n = [0, 1, 2, 4, 5, 7]
    # n = [0, 2, 3, 4, 6, 8, 9]
    print(summaryranges(n))

