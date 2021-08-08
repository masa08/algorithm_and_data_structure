def stockSpan(stocks):
    stack = []
    result = []

    for price in stocks:
        count = 1
        for prevPrice in reversed(stack):
            if prevPrice <= price: count += 1
            else: break
        stack.append(price)
        result.append(count)

    return result
