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



# For inputArray = [3, 6, -2, -5, 7, 3], the output should be
# adjacentElementsProduct(inputArray) = 21.
def adjacentElementsProduct(inputArray):
    current = -100000
    for i in range(len(inputArray) - 1):
        if inputArray[i] * inputArray[i + 1] > current:
            current = inputArray[i] * inputArray[i + 1]
            
    return current
        
def adjacentElementsProduct2(inputArray):
    return max([inputArray[i] * inputArray[i+1] for i in range(len(inputArray)-1)])

# 1 -> 5 -> 13 -> 25 -> 41 -> ...
# 1 + 4 + 8 + 12 + 16 + 4*count
def shapeArea(n):
    current = 1
    count = 1
    while count < n:
        current += 4*count
        count += 1

    return current

def shapeArea2(n):
    return n**2 + (n-1)**2

