#RECURSION
import time
#iterative method using for loop
# t = time.time()
def sumNum(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    # return int(n*(n+1)/2)
    return sum
# print(sumNum(900))
# print('COmpletion time for iterative :', time.time() - t)
#recursive method
# ti = time.time()
#sum of natural number
def recSum(n):
    if n == 1: return 1
    return n + recSum(n-1)
# print(recSum(900))
# print('COmpletion time for recursive :', time.time() - ti)

#fibonacci number
# 0, 1, 1, 2, 3, 5, 8
# 0  1  2  3  4  5  6
def fib(n):
    if n == 0 or n == 1: return n
    return fib(n-1) + fib(n-2)
# print(fib(1))

# https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion-exercise-1.php
# 1. Write a Python program to calculate the sum of a list of numbers.
arr = [i for i in range(1, 21)]
def sum20(arr):
    # return arr[0] if len(arr) == 1 else arr[0] + sum20(arr[1:])
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum20(arr[1:])
# print(sum20(arr))

# 2. Write a Python program to converting an Integer to a string in any base
def toStr(n, base):
    toSr = '0123456789ABCDEF'
    if n < base:
        return toSr[n]
    else:
        return toStr((n // base), base) + toSr[n % base]
# print(toStr(256, 16))

# 3. Write a Python program of recursion list sum.
# Test Data: [1, 2, [3,4], [5,6]]
# Expected Result: 21
def listSum(arr):
    total = 0
    for el in arr:
        if type(el) == list:
            total += listSum(el)
        else:
            total += el
    return total
# print(listSum([[3, 4], [5, 6], 5, 23]))

# 4. Write a Python program to get the factorial of a non-negative integer.
def fact(n):
    if n == 1: return 1
    # 4*3*2*1
    else:
        return n * fact(n-1)
# print(fact(4))

# 5. Write a Python program to solve the Fibonacci sequence using recursion.
def fib(n):
    if n == 0 or n == 1: return n
    else:
        return fib(n-2) + fib(n-1) 
# print(fib(6))

# 6. Write a Python program to get the sum of a non-negative integer. 
# Test Data:
# sumDigits(345) -> 12
# sumDigits(45) -> 9 
def sumDigits(n):
    if n == 0: return 0
    else:
        return n % 10 + sumDigits(n // 10)
# print(sumDigits(345))
# print(sumDigits(45))

# 7. Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0).
# Test Data:
# sum_series(6) -> 12
# sum_series(10) -> 30 
def sum_series(n):
    if n == 0: return 0
    else:
        return n + sum_series(n-2)
# print(sum_series(6))
# print(sum_series(10))

# 8. Write a Python program to calculate the harmonic sum of n-1. 
# Note: The harmonic sum is the sum of reciprocals of the positive integers.
# Example :
# 1 + 1/2 + 1/3 + 1/4 + 1/5 + ..................
def harmonic_sum(n):
    if n <= 1: return 1
    else:
        return 1 / n + harmonic_sum(n - 1)
# print(harmonic_sum(7))
# print(harmonic_sum(0))

# Write a Python program to calculate the geometric sum of n-1. Go to the editor
# Note: In mathematics, a geometric series is a series with a constant ratio between successive terms.
def geometric_sum(n):
    if n < 0:
        return 0
    else:
        return 1 / pow(2, n) + geometric_sum(n - 1)
# print(geometric_sum(7))
# print(geometric_sum(4))

# 10. Write a Python program to calculate the value of 'a' to the power 'b'. Go to the editor
# Test Data :
# (power(3,4) -> 81 
def power(a, b):
    if b == 0: return 1
    elif a == 0: return 0
    elif b == 1: return a
    else: return a * power(a, b-1) 
# print(power(3, 4))

# 11. Write a Python program to find  the greatest common divisor (gcd) of two integers
def recGcd(a, b):
    low = min(a, b)
    high = max(a, b)
    if low == 0: return high
    elif low == 1: return 1
    else: return recGcd(low, high % low)
print(recGcd(72, 64))