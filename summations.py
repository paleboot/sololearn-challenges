"""
Takes 3 inputs, a lower bound, an upper bound, and the expression. Calculate the sum of that range based on the given expression and output of the result.

Example:
Input: 2 4*2
Output: 18(2*2 + 3*2 + 4*2)

Input: 1 5%2
Output: 3(1%2 + 2%2 + 3%2 + 4%2 + 5%2)
"""
ops = {
    "+": (lambda x,y: x+y),
    "-": (lambda x,y: x-y),
    "/": (lambda x,y: x/y),
    "*": (lambda x,y: x*y),
    "%": (lambda x,y: x%y),
}
testInput = input("Input: ")
testInput.split()
lowerBound = int(testInput[0])
upperBound = int(testInput[2])
result = 0
for i in range(lowerBound, upperBound+1):
    result += ops[testInput[4]](i,int(testInput[-1]))

print(result)
