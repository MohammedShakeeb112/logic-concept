# Write a program to input 2 numbers and display the sum of the numbers to the console.
# Input Number 1: 20
# Input Number 2: 40
# Sum : 60
def sumTwo(m,n):
    return f'Sum : {m+n}'
# m,n = int(input('Input Number 1: ')), int(input('Input Number 2: '))
# print(sumTwo(m,n))

# Write a JavaScript program to calculate the simple interest given P,R,T with the given formula. Formula: SI = (P * T * R) / 100 Where: P = principal amount T = time R = rate SI = simple interest
# Input: P=100, R=6%, T=2
# Output: 12
def si(p, r, t):
    si = int((p*r*t)/100)
    return si
# p, r, t = int(input('Enter the pricipal amount ')), int(input('Enter the rate of interest ')), int(input('Enter the time '))
# print(si(p, r, t))

# Write a program to calculate the kinetic energy of a body with mass 'm' and volume 'v'.
# Formula : 0.5 * m * v * v
def kineticEnergy(m, v):
    ke = 0.5 * m * v * v
    return ke
# m,v = int(input('Enter the mass of the body ')), int(input('Enter the volume '))
# print(kineticEnergy(m,v))

# Write a program to convert Fahrenheit to Celsius. For Fahrenheit to Celsius conversion use: C = (F - 32) * 5/9 'F' and 'C' are the temperatures on the Fahrenheit scale and Celsius scale respectively.
# Input: 56
# Output: 13.33333
def fah_Cel(f):
    c = (f - 32) * 5/9
    return c
# print(fah_Cel(56))



# Calculate the area, perimeter of a square of side 'a'. Also, calculate the surface area and the volume of a cube of side 'a'.
# Formula :
# Area: a*a
# Perimeter: 4*a
# Surface Area: 6*a*a
# Volume: a*a*a
def square(a):
    area = a * a
    perimeter = 4 * a
    surface_area = 6 * a * a
    volume = a * a * a
    return f'area of square is : {area}, perimeter of square is : {perimeter}, surface_area of square is : {surface_area}, volume of square is : {volume}'
# print(square(15)) 

# Given the Cost Price(CP) and Selling Price(SP) of a product. Write a Program to Calculate the Profit or Loss.
# Input: CP = 1500, SP = 2000
# Output: 500 Profit

# Input: CP = 3125, SP = 1125
# Output: 2000 Loss
def pl(cp, sp):
    if cp > sp:
        return f'{cp-sp} Loss'
    else:
        return f'{sp-cp} Profit'
# print(pl(1500, 2000))
# print(pl(3125, 1125))

# Write a program to calculate sum of N natural digits, as input by the users?
# Enter a positive integer: 100
# Sum = 5050
def sumNat(n):
    if n <= 0: return 
    if n == 1: return 1
    return sumNat(n-1)+n #resursive call
    # return int(n*(n+1)/2)
# print(sumNat(100))

# Write a Program to Print N Odd Number in Descending Order.
# Input : 4
# Output : 7
# 5
# 3
# 1
def odd_des(n):
   for i in range(n*2-1, 0, -2):
        print(i)
# odd_des(4)

# Write a JavaScript program to compute the sum of all digits that occur in a given string.
# Input: 1234
# Output: 1+2+3+4 = 10
def strInt(s):
    s = list(s)
    res = []
    for i in s:
        res.append(int(i))
    resSum = sum(res)
    return resSum
# print(strInt('1234'))

# Write a JavaScript program that reverses a number.
# Input:  32243;
# Output:  34223
def revNum(n):
    result = int(str(n)[-2:][::-1] + str(n)[:-2][::-1])
    return result
# print(revNum(32243))

# Write a Program to cyclically Rotate a Number by X positions in the left direction, as provided by the user.
# Example-
# Enter a Number : 1234
# Enter the Number of Rotations : 2
# Output : 3412
def rotateNum(n):
    l = str(n)
    return int(l[::-1][:-2][::-1]+l[::-1][-2:][::-1])
    
# print(rotateNum(1234))

# Write a Program to convert Decimal to Binary.
# Enter the number to convert: 5
# Binary of Given Number is=101
def decBin(n):
    return bin(n)[2:]
# print(decBin(5))

# Follow up Question : Write a Program to Convert Octal to Decimal.
# Enter an octal number: 116
# Octal of Given Number = 78 in decimal
def octDec(n):
    # return int(n ,8)
    temp = int(n)
    dec_val = 0
    base = 1
    while temp:
        last_digit = temp % 10
        dec_val += last_digit * base
        base *= 8
        temp //= 10
    return dec_val
print(octDec('116'))