def missingItems(listA, listB):
    itemLists = []
    for a in listA:
        if a not in listB:
            itemLists.append(a)

    return itemLists
