def reachNextLevel(experience, threshold, reward):
    return experience + reward >= threshold

def knapsackLight(value1, weight1, value2, weight2, maxW):
    if weight1 + weight2 <= maxW:
        return value1 + value2
    else:
        return max(value1 if weight1 <= maxW else 0, value2 if weight2 <= maxW else 0)

def extraNumber(a, b, c):
    return a if b == c else b if a == c else c

def isInfiniteProcess(a, b):
    return True if a > b else True if (b-a) % 2 != 0 else False

def arithmeticExpression(a, b, c):
    return True if a + b == c or a - b == c or a * b == c or a / b == c else False

def arithmeticExpression2(a, b, c):
    return c in (a+b, a-b, a*b, a/b)

def arithmeticExpression3(A, B, C):
    return any([
        A + B == C,
        A - B == C,
        A * B == C,
        A / B == C])

def tennisSet(score1, score2):
    return sorted((score1, score2)) in ([6, 7], [5, 7], [4, 6], [3, 6], [2, 6], [1, 6], [0, 6])
