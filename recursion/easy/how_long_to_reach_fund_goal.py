def howLongToReachFundGoal(capitalMoney, goalMoney, interest):
    def _howLongToReachFundGoal(capitalMoney, goalMoney, interest, year):
        if year > 80:
            return 80
        if capitalMoney >= goalMoney:
            return year

        if year % 2 == 0:
            goalMoney *= 1.02
        else:
            goalMoney *= 1.03

        capitalMoney *= 1 + interest/100
        year += 1

        return _howLongToReachFundGoal(capitalMoney, goalMoney, interest, year)

    return _howLongToReachFundGoal(capitalMoney, goalMoney, interest, 0)
