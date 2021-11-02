# https://leetcode.com/problems/happy-number/

def ishappy(n):
    s = []

    def foo(num):
        if num == 1:
            return True
        else:
            tmp = 0
            while num > 0:
                tmp += pow(num % 10, 2)
                num = num // 10
            if tmp in s:
                return False
            else:
                s.append(tmp)
                return foo(tmp)
    return foo(n)


if __name__ == '__main__':
    num = 17
    print(ishappy(num))
