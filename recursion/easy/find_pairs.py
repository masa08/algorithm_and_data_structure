def findPairs(numbers):
    hashmap = {}
    result = []
    for number in numbers:
        if number in hashmap:
            hashmap[number] += 1
        else:
            hashmap[number] = 1
    for k, v in hashmap.items():
        if v == 2:
            result.append(k)

    return sorted(result)
