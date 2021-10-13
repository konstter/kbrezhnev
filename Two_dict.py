
def two_dict(dict1, dict2, path):
    for key, value in dict1.items():
        path += key
        if isinstance(value, dict):
            path += ' -> '
            return two_dict(dict1[key], dict2[key], path)
        else:
            if isinstance(value, list):
                dict1[key].sort()
                dict2[key].sort()
            if dict1[key] != dict2[key]:
                print(path)
            else:
                path = ''



d1 = { 'a':1, 'b': { 'c': { 'd': 1 } }, 'e': { 'f': { 'g': 2 } } }
d2 = { 'a':1, 'b': { 'c': { 'd': 2 } }, 'e': { 'f': { 'g': 1 } } }

two_dict(d1, d2, '')
