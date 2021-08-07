
class Player:
    def __init__(self, name, dices):
        self.name = name
        self.dices = dices
        self.money = self.calcMoney(dices)

    def getName(self):
        return self.name

    def getMoney(self):
        return self.money

    def getMoneyString(self):
        return str(self.money)

    def getDices(self):
        return self.dices

    def getDiceString(self):
        result = "["
        for d in self.dices:
            if d == self.dices[-1]: result += str(d) + "]"
            else: result += str(d) + ","

        return result

    def calcMoney(self, dices):
        exMoney = 0
        result = 0
        for i, d in enumerate(dices):
            if d >= exMoney: result += 4
            else:
                result = 4
                self.dices = dices[i:]
            exMoney = d

        return result

def checkWinner(players):
    hashmap = {}
    for i, player in enumerate(players):
        hashmap[i] = player.getMoney()
    winnerKey = max(hashmap, key=hashmap.get)

    return players[winnerKey]

def diceStreakGamble(player1,player2,player3,player4):
    players = [
        Player("Player 1", player1),
        Player("Player 2", player2),
        Player("Player 3", player3),
        Player("Player 4", player4)
    ]
    winner = checkWinner(players)

    return "Winner: " + winner.getName() + " won $" + winner.getMoneyString() + " by rolling " + winner.getDiceString()
