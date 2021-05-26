def isMountain(height):
    if len(height) <= 2 or height[0] > height[1] or height[-1] == max(height):
        return False
    lastIndex = len(height) - 1
    currentIndex = 0
    currentHeight = height[0]

    while currentHeight != max(height):
        currentIndex += 1
        nextHeight = height[currentIndex]
        if currentHeight >= nextHeight:
            return False
        currentHeight = nextHeight

    while currentIndex != lastIndex:
        currentIndex += 1
        nextHeight = height[currentIndex]
        if currentHeight <= nextHeight:
            return False
        currentHeight = nextHeight

    return True
