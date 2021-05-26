def hasPenalty(records):
    previousRecord = records[0]
    for record in records[1:]:
        if record < previousRecord:
            return True
        previousRecord = record

    return False
