

def two_dict(dict1, dict2, path):
    l = list(dict1.keys())
    for item in l:
        path += item
        if isinstance(dict1[item], dict):
            path += ' -> '
            return two_dict(dict1[item], dict2[item], path)
        else:
            if isinstance(dict1[item], list):
                dict1[item].sort()
                dict2[item].sort()
            if dict1[item] != dict2[item]:
                print(path)
            else:
                path = ''




d1 = { 'a':1, 'b': { 'c': { 'd': 1 } }, 'e': { 'f': { 'g': 2 } } }
d2 = { 'a':1, 'b': { 'c': { 'd': 2 } }, 'e': { 'f': { 'g': 1 } } }

two_dict(d1, d2, '')
