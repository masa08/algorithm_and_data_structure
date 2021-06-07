def winnerPairOfCards(player1, player2):
    player1_cards = {}
    player2_cards = {}
    rank = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
            "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    # 手札がなくなった場合はdraw
    if not player1 and not player2:
        return "draw"
    # 手札を連想配列に格納
    for card1 in player1:
        if card1[1:] in player1_cards:
            player1_cards[card1[1:]] += 1
        else:
            player1_cards[card1[1:]] = 1
    for card2 in player2:
        if card2[1:] in player2_cards:
            player2_cards[card2[1:]] += 1
        else:
            player2_cards[card2[1:]] = 1
    # 最大枚数を比較
    max1 = max(player1_cards.values())
    max2 = max(player2_cards.values())
    if max1 > max2:
        return "player1"
    if max1 < max2:
        return "player2"
    # 最大枚数が同じだった場合はランクで比較
    else:
        card1 = [k for k, v in player1_cards.items() if v == max1]
        card2 = [k for k, v in player2_cards.items() if v == max2]
        maxr1 = 0
        high_card1 = ""
        for card in card1:
            r = rank[card]
            if r > maxr1:
                high_card1 = card
                maxr1 = r
        maxr2 = 0
        high_card2 = ""
        for card in card2:
            r = rank[card]
            if r > maxr2:
                high_card2 = card
                maxr2 = r

        rank1 = high_card1
        rank2 = high_card2
        if rank[rank1] > rank[rank2]:
            return "player1"
        elif rank[rank1] < rank[rank2]:
            return "player2"
        else:
            player1 = [p for p in player1 if p[1:] != high_card1[0]]
            player2 = [p for p in player2 if p[1:] != high_card2[0]]

    return winnerPairOfCards(player1, player2)
