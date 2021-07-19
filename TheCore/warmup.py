# Little things that could be useful

def addTwoDigits(n):
    return int(str(n)[0]) + int(str(n)[1])

def largestNumber(n):
    return int("9" * n)

def candies(n, m):
    return m - (m % n) # 10 - 1


# the results of modulo when the first number is smaller. The result is always equal the the first (smaller) number

# 3 % 5 = 3
# 5 % 10 = 5
# 78 % 112 = 78

def circleOfNumbers(n, firstNumber):
    return (firstNumber + n / 2) % n
