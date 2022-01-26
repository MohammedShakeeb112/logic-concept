# Write a program to add 5 numbers. The value of numbers are num1=5, num2=13, num3=7, num4=21 and num5=48
def add5N(n1,n2,n3,n4,n5):
    val = n1+n2+n3+n4+n5
    return val
# n1, n2, n3, n4, n5 = 5, 13, 7, 21, 48
# n1, n2, n3, n4, n5 = int(input('Enter the no.')),int(input('Enter the no.')),int(input('Enter the no.')),int(input('Enter the no.')),int(input('Enter the no.'))
# print(add5N(n1, n2, n3, n4, n5))

# Write a program to take a number input from user and determine whether the number is odd or even.
def oddEven(n):
    if not n:
        return 
    if n % 2 == 0:
        return 'EVEN'
    else:
        return 'ODD'
# n = int(input('Enter the no.'))
# print(oddEven(n))

# Write a program to find the maximum and minimum out of two given numbers. The numbers are num1=129 and num2=251.
def maxMin(m, n):
    maxV = max(m, n)
    minV = min(m, n)
    return f'maxValue : {maxV}, minValue : {minV}'
# m,n = int(input('Enter the no.')), int(input('Enter the no.'))
# print(maxMin(m, n))

# Write a program to find the maximum out of three given numbers. The numbers are num1=8, num2=23 and num3=17.
def maxthree(n1,n2,n3):
    maxValue = max(n1, max(n2, n3))
    return maxValue
# n1,n2,n3 = int(input('Enter the no.')),int(input('Enter the no.')),int(input('Enter the no.'))
# print(maxthree(n1,n2,n3))

# Write a program to find the minimum out of three given numbers. The numbers are num1=35, num2=29 and num3=46.
def minthree(n1,n2,n3):
    minValue = min(n1, min(n2,n3))
    return minValue
# n1,n2,n3 = int(input('Enter the no.')),int(input('Enter the no.')),int(input('Enter the no.'))
# print(minthree(n1,n2,n3))

# Write program to take a month as an input from the user and find out whether the month has 31 days or not.
def month_days(n):
    dic = {1:'January : 31 Days', 2:'February : 28/29 Days', 3:'March : 31 Days', 4:'April : 30 Days', 5:'May : 31 Days', 6:'June : 30 Days', 7:'July : 31 Days', 8:'August : 31 Days', 9:'September : 30 Days', 10:'October : 31 Days', 11:'November : 30 Days', 12:'December : 31 Days'}
    if n not in dic:
        return 'Invalid month, try again'
    return dic[n]
# n = int(input('enter the month in integer : '))
# print(month_days(n))

# Fizzbuzz - Write a program to return an array from 1 to 100. But for every multiple of 3, replace the number with "Fizz", for every multiple of 5, replace the number with "Buzz" and for every multiples of 3 & 5, replace with "FizzBuzz".
# Your output should look something like this 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16, 17 ..... 
def fizz_buzz(n):
    for i in range(1, n+1):
        if i % 15 == 0:
            print('FizzBuzz')
            continue
        elif i % 3 == 0:
            print('Fizz')
            continue
        elif i % 5 == 0:
            print('Buzz')
            continue
        print(i)

# fizz_buzz(100)



# Print the following star pattern :-

# *
# * *
# * * *
# * * * *
# * * * * *

def pattern(n):
    for i in range(n):
        for j in range(i+1):
            print('*', end=' ')
        print()
        
# pattern(5)

# Write a program to take a number input from user and print multiplication table 12 times for that number.
def mult(n):
    for i in range(1,13):
        print(f'{n} * {i} = {i*n}')
# n = int(input('enter the no. '))
# mult(n)

# Write a program to return a Fibonacci series : 0,1,1,2,3,5,8,13,21....
def fibonacci(n):
    if n <0: return
    elif n == 0: return 0
    elif n == 1: return 1
    return fibonacci(n-1) + fibonacci(n-2)
        
# n = int(input('enter the no. '))
# print(fibonacci(n))

# Write a program to take an input from a user and find its Factorial. Example: Factorial of 5 is 120
def factorial(n):
    if n < 0: return
    elif n == 1: return 1
    return factorial(n-1) * n

# n = int(input('enter the no. '))
# print(factorial(n))

# Write a Program to take a number input from user and find if the number is Prime or not.
def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
def primeGen(n):
    num = 2
    while n:
        if isPrime(num):
            yield num
            n -= 1
        num += 1
    return

# n = int(input('enter the no. '))
# it = primeGen(n)
# ls = []
# for i in it:
#     ls.append(i)
# print(ls)

# Write a program to take a day as an input and determine whether it is a weekday or weekend. Example: Tuesday is weekday.
def days(n):
    n = n.capitalize()
    if n == 'Saturday' or n == 'Sunday':
        return f'{n} is Weekend'
    else:
        return f'{n} is Weekday'
n = input('enter the day ')
print(days(n))