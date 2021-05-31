def findXTimes(teams):
    hashmap = {}
    for team in teams:
        if team in hashmap:
            hashmap[team] += 1
        else:
            hashmap[team] = 1
    return max(hashmap.values()) == min(hashmap.values())

    # count = hashmap[teams[0]]
    # for k, v in hashmap.items():
    #     if v != count: return False
    # return True
