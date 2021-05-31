def intersectionOfArraysRepeats(intList1, intList2):
    hashmap = {}
    result = []
    for i in range(len(intList1)):
        if intList1[i] in hashmap:
            hashmap[intList1[i]] += 1
        else:
            hashmap[intList1[i]] = 1

    for j in range(len(intList2)):
        if intList2[j] in hashmap and hashmap[intList2[j]] > 0:
            result.append(intList2[j])
            hashmap[intList2[j]] -= 1

    return sorted(result)
