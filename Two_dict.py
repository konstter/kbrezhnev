
def two_dict(dict1, dict2):
    def rec(dict1, dict2):
        l = list(dict1.keys())
        for item in l:
            t1, t2 = type(dict1[item]), type(dict2[item])
            if t1 != t2:
                return False
            else:
                if t1 != dict:
                    if t1 == list:
                        dict1[item].sort()
                        dict2[item].sort()
                    if dict1[item] != dict2[item]:
                        return False
                else:
                    return rec(dict1[item], dict2[item])
    fl = rec(dict1, dict2)
    return fl != False


d1 = { 'a':1, 'b': { 'c': 1 } }
d2 = { 'a':1, 'b': { 'c': 1 } }

# d1 = d2 = {i: i + 1 for i in range(7)}
print(two_dict(d1, d2))

