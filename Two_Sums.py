

def twoSum(nums, target):
    '''
    :param nums: List[int]
    :param target: int
    :return: List[int]
    '''
    temp_dict = dict([(k, nums[k]) for k in range(len(nums))])
    sorted_dict = {}
    sorted_keys = sorted(temp_dict, key=temp_dict.get)
    for w in sorted_keys:
        sorted_dict[w] = temp_dict[w]
    i = 0
    j = -1
    output_list = []
    while True:
        if list(sorted_dict.values())[i] + list(sorted_dict.values())[j] == target:
            output_list.append(list(sorted_dict.keys())[i])
            output_list.append(list(sorted_dict.keys())[j])
            return output_list
        elif list(sorted_dict.values())[i] + list(sorted_dict.values())[j] < target:
            i += 1
        else:
            j -= 1


# n = [3, 3]
# t = 6

n = [1, 2, 10, 7, 8]
t = 15

print(twoSum(n, t))


