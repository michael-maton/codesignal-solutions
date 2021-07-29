def reachNextLevel(experience, threshold, reward):
    return experience + reward >= threshold

def knapsackLight(value1, weight1, value2, weight2, maxW):
    if weight1 + weight2 <= maxW:
        return value1 + value2
    else:
        return max(value1 if weight1 <= maxW else 0, value2 if weight2 <= maxW else 0)

def extraNumber(a, b, c):
    return a if b == c else b if a == c else c