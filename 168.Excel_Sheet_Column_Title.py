# https://leetcode.com/problems/excel-sheet-column-title/

def converttotitle(columnnumber):
    column_letters = {0: 'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J', 10:'K', 11:'L',
                      12:'M', 13:'N', 14:'O', 15:'P', 16:'Q', 17:'R', 18:'S', 19:'T', 20:'U', 21:'V',
                      22:'W', 23:'X', 24:'Y', 25:'Z', -1: 'Z' }
    def foo(num):
        if num < 26:
            return column_letters[num - 1]
        q, r = num // 26, num % 26
        if r == 0:
            if q == 1:
                return column_letters[r-1]
            else:
                return foo(q-1) + column_letters[r-1]
        else:
            return foo(q) + column_letters[r-1]
    return foo(columnnumber)


if __name__=='__main__':
    cn = 28
    print(converttotitle(cn))


