# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

def twosum(numbers, target):
    i, j = 0, len(numbers) - 1
    while True:
        if numbers[i] + numbers[j] == target:
            return [i + 1, j + 1]
        elif numbers[i] + numbers[j] > target:
            j -= 1
        else:
            i += 1


if __name__ == '__main__':
    n = [2, 7, 11, 15]
    t = 9
    print(twosum(n, t))
