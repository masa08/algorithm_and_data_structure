def winnerBlackjack(playerCards, houseCards):
    playerPoint = countPoint(playerCards)
    housePoint = countPoint(houseCards)
    if playerPoint > 21 or (playerPoint == housePoint) or (housePoint < 22 and housePoint > playerPoint):
        return False

    return True


def countPoint(cards):
    mapping = {"A": 1, "J": 11, "Q": 12, "K": 13}
    count = 0
    for card in cards:
        if card[1] in mapping:
            count += mapping[card[1:]]
        else:
            count += int(card[1:])
    return count
