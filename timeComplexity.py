# airthmetic operation => 1 operation time
# addition/subtraction/multiplication/division operation => 1 operation time
# comparison operation => 1 operation time
# return operation => 1 operation time

num = [3,6,2,4,3,6,8,9]
dup = None
for i in range(len(num)):   #n iteration
    for j in range(i+1, len(num)):  #n iteration
        if num[i] == num[j]:
            dup = num[i]
            break           #n2 iteration => a*n2+b =>o(n2) 
# print(dup)
# for i in range(len(num)): #n iteration => a*n+b => o(n)
#     if num[i] == dup:
#         print(i)
#   a*n2+b*n+c => o(n2)+o(n) => o(n2) 

import time
arr = [4,9,15,21,34,57,68,91]
t = time.time()
#search 68
# 1. linear search O(n)
# for i in range(len(arr)):
#     if arr[i] == 68:
#         print(i)
# print('linear search time completion:', time.time() - t)
# operation in linear search 
# input size(n)   operations 
#   10              
#        
#2. binary search
ti = time.time()
def search(arr, l, r, n):
    while l <= r:
        mid = (l+r)//2
        if arr[mid] == n:
            return mid
        if arr[mid] < n:
            l = mid + 1
        else:
            r = mid - 1
    return -1

# print(search(arr, 0, len(arr)-1, 68))
# print('binary search time completion:', time.time() - ti)


# Constant Time COmplexity O(1)
def fun(x): # total 4 operation
    x = x + 1      # 2 opeartion
    return x*5     # 2 operation
fun(1)    #4 operation constant time
fun(100000)   #4 operation constant time

def sumNat(n): #O(n)
    total = 0
    for i in n:
        total += i
    return total
print(sumNat([i for i in range(1,20)]))


# comaprision using time complexcity
# |_n      ^
# 2^n      |
# n^2      |
# nlogn    |
# n        |
# root n   |
# logn     |
# 1        | increasing

# t1 = 2^n + 27root(n) + 33 => t1 = 2^n
# t2 = nlogn + 72 = t2 = nlogn
# t2 is better

code = {}
N = 3
def print_code(pos):
    if pos == N:
        print(code)
        return
    code[pos] = 0
    print_code(pos+1)
    code[pos] = 1
    print_code(pos+1)

print_code(0)