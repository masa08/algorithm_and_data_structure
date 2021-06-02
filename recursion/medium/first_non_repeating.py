def firstNonRepeating(string):
    hashmap = {}
    for c in string:
        if c not in hashmap:
            hashmap[c] = 1
        else:
            hashmap[c] += 1
    for k, v in hashmap.items():
        if v == 1:
            return string.index(k)

    return -1
