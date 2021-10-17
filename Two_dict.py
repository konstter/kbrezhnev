
def two_dict(dict1, dict2, path):
    for key, value in dict1.items():
        if isinstance(value, dict):
            path += key + ' -> '
            two_dict(dict1[key], dict2[key], path)
        else:
            if isinstance(value, list):
                dict1[key].sort()
                dict2[key].sort()
            if dict1[key] != dict2[key]:
                path += key
                print(path)
        path = ''


d1 = { 'b': { 'c': { 'd': 2 } }, 'e': { 'f': { 'g': 2 } }, 'h' : { 'i': [3, 2, 2] }, 'k': 1 }
d2 = { 'b': { 'c': { 'd': 1 } }, 'e': { 'f': { 'g': 1 } } , 'h' : { 'i': [2, 1, 3] }, 'k': 1 }

two_dict(d1, d2, '')
