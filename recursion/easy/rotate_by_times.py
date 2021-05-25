# nをidsのlengthで割った余りが移動の数m
# mで配列を分裂させて、再度配列を生成する
def rotateByTimes(ids, n):
    moveNumber = n % len(ids)
    formerIds, latterIds = ids[-moveNumber:], ids[:-moveNumber]
    return formerIds + latterIds
