"""
Gapful Number
Number of at least 3 digits that is divisible by the number formed by the first and last digit of the original number

example:
Input: 192
Output: true (192 is gapful because it is divisible by 12)

Input: 210
Output: false(210 is not gapful because it is not divisible by 20)
"""

def gapfulNumber(num):
    numString = str(num)
    divisor = numString[0] + numString[-1]
    print(divisor)
    if (num%int(divisor) == 0):
        print("true")
    else:
        print("false")
x = int(input("Input a number of at least 3 digits: "))
gapfulNumber(x)