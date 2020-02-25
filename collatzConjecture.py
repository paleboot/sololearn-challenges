"""
1. Take any natural number
2. If it's even, half it, otherwise triple it and add one
3. Repeat step 2, until you reach 4, 2, 1 sequence
4. You will ALWAYS reach 1, eventually.

Example:

x = 17
17*3+1 = 52
52/2 = 26
26/2 = 13
13*3+1 = 40
40/2 = 20
20/2 = 10
10/2 = 5
5*3+1 = 16
16/2 = 8
8/2 = 4
4/2 = 2
2/2 = 1

"""
def collatzConjecture(num):
    while(num!=1):
        if (num%2 == 0):
            num = num//2
            print(num)           
        elif(num%2 == 1):
            num = num*3+1
            print(num)           
x = int(input("Insert natural number: "))
collatzConjecture(x)