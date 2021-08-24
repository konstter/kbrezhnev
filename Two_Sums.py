

def twoSum(nums, target):
    '''
    :param nums: List[int]
    :param target: int
    :return: List[int]
    '''
    output_list = []
    j = 0
    while j < len(nums):
        for i in range(len(nums)):
            if i != j:
                if nums[i] + nums[j] == target:
                    if i < j:
                        output_list.append(i)
                        output_list.append(j)
                    else:
                        output_list.append(j)
                        output_list.append(i)
                    return output_list
        j +=1


n = [3, 2, 7, 1, 8]
t = 15

print(twoSum(n, t))

# n = [2, 7, 11, 15]
# t = 9

# n = [3, 2, 4]
# t = 6

# n = [3, 3]
# t = 6

