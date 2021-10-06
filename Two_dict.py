
def two_dict(dict1, dict2):
    l = list(dict1.keys())

    def rec(l):
        if not l:
            return True
        if dict1[l[-1]] != dict2[l[-1]]:
            return False
        l.pop()
        return rec(l)
    return rec(l)


d1 = {'a': 'string', 'b': 5, 'c': [0, 1], 'd':{}}
d2 = {'c': [0, 1], 'a': 'string', 'd':{}, 'b': 5}

# d1 = d2 = {i: i + 1 for i in range(7)}
print(two_dict(d1, d2))

