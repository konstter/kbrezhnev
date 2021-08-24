

def twoSum(nums, target):
    '''
    :param nums: List[int]
    :param target: int
    :return: List[int]
    '''
    temp_dict = {}
    for i in range(len(nums)):
        temp_dict[nums[i]] = i
    nums.sort()
    i = 0
    j = -1
    output_list = []
    while True:
        if nums[i] + nums[j] == target:
            output_list.append(temp_dict.get(nums[i]))
            output_list.append(temp_dict.get(nums[j]))
            return output_list
        elif nums[i] + nums[j] < target:
            i += 1
        else:
            j -= 1


n = [1, 2, 10, 7, 8]
t = 15

print(twoSum(n, t))


