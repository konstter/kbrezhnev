

def twoSum(nums, target):
    '''
    :param nums: List[int]
    :param target: int
    :return: List[int]
    '''
    cache_list = nums.copy()
    nums.sort()
    i = 0
    j = -1
    output_list = []
    while True:
        if nums[i] + nums[j] == target:
            output_list.append(cache_list.index(nums[i]))
            cache_list[cache_list.index(nums[i])] = 'used'
            output_list.append(cache_list.index(nums[j]))
            return output_list
        elif nums[i] + nums[j] < target:
            i += 1
        else:
            j -= 1


n = [3, 3]
t = 6

# n = [1, 2, 10, 7, 8]
# t = 15

print(twoSum(n, t))


