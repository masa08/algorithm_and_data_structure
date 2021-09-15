function maxProfit(prices: number[]): number {
    let max_profit = 0
    let min_price = Number.MAX_SAFE_INTEGER

    for (let price of prices) {
        min_price = Math.min(min_price, price)
        max_profit = Math.max(max_profit, price - min_price)
    }

    return max_profit
};
