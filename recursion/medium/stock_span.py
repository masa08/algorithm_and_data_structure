# O(n**2)
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

# O(n)
def stockSpan(stocks):
    stack = []  # indexを保持
    result = [] # countを保持

    for i, price in enumerate(stocks):
        count = 1
        while stack and stocks[stack[-1]] < price:
            top = stack.pop()
            count += result[top]

        result.append(count)
        stack.append(i)

    return result
