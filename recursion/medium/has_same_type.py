def hasSameType(user1, user2):
    if len(user1) != len(user2):
        return False
    hashmap = {}
    for i in range(len(user1)):
        if user1[i] not in hashmap and user2[i] not in hashmap.values():
            hashmap[user1[i]] = user2[i]
    string = ""
    for user in user1:
        if user in hashmap:
            string += hashmap[user]
        else:
            return False
    if string != user2:
        return False

    return True
