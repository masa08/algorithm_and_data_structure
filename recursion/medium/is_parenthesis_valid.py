def isParenthesesValid(parentheses):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for p in parentheses:
        if p in mapping:
            top_element = stack.pop() if stack else ''
            if top_element != mapping[p]:
                return False
        else:
            stack.append(p)
    return True
