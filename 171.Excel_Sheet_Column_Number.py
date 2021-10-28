# https://leetcode.com/problems/excel-sheet-column-number/

def titletonumber(columntitle):
    column_nums = { 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
                      'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22,
                      'W': 23, 'X': 24, 'Y': 25, 'Z': 26 }
    r_title = columntitle[::-1]
    title_num, i, lt = 0, 0, len(columntitle)
    while i < lt:
        title_num += column_nums[r_title[i]] * pow(26, i)
        i += 1
    return title_num



if __name__ == '__main__':
    # ct = 'ZY'
    # ct = 'FXSHRXW'
    ct = 'A'
    print(titletonumber(ct))
