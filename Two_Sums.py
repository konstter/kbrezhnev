

def twoSum(nums, target):
    '''
    :param nums: List[int]
    :param target: int
    :return: List[int]
    '''
    index_list = [k for k in range(len(nums))]
    num = zip(nums, index_list)
    sorted_list = sorted(num, key=lambda tup: tup[0])
    i = 0
    j = -1
    output_list = []
    while True:
        if sorted_list[i][0] + sorted_list[j][0] == target:
            output_list.append(sorted_list[i][1])
            output_list.append(sorted_list[j][1])
            return output_list
        elif sorted_list[i][0] + sorted_list[j][0] < target:
            i += 1
        else:
            j -= 1


# n = [3, 3]
# t = 6

n = [1, 2, 10, 7, 8]
t = 15

print(twoSum(n, t))


