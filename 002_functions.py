# Given a and b, your function should return the value of ab
# Example:
# Input: power(2,3) ––> Output: 8
import math 
def power(a, b):
    # return a**b
    return int(math.pow(a, b))
# print(power(2,3))

# Given length of a regular hexagon, your function should return area of the hexagon.
# Example:
# Input: areaOfHexagon(10) ––> Output: 259.80
#area = ((3*3)*length**2)/2
def areaofhex(n):
    area = round(((3*math.sqrt(3))/2)*n**2,2)
    return area
# print(areaofhex(10))

# Given a sentence, your functions should return the number of words in the sentence.
# Example:
# Input: noOfWords(We are neoGrammers) ––> Output: 3
def noOfWords(n):
    word = n.strip().split()
    return len(word)
# print(noOfWords('We are neoGrammers'))

# Given n numbers, your function should return the minimum of them all. The number of parameters won't be accepted from user.
# Example:
# Input: findMin(3,5) ––> Output: 3
# Input: findMin(3,5,9,1) ––> Output: 1
def findMin(*args):
    val = []
    for i in args:
        val.append(i)
    val.sort()
    return val[0]
# print(findMin(3,5))
# print(findMin(3,5,9,1))

# Given n numbers, your function should return the maximum of them all. The number of parameters won't be accepted from user.
# Example:
# Input: findMax(3,5) ––> Output: 5
# Input: findMax(3,5,9,1) ––> Output: 9
def findMax(*args):
    val = []
    for i in args:
        val.append(i)
    val.sort(reverse=True)
    return val[0]
# print(findMax(3,5))
# print(findMax(3,5,9,1))

# Given three angles of a triange, your function should return if it is a scalen, isosceles, equilateral triangle or not a triangle at all. Example:
# Input: typeOfTriangle(30, 60, 90) ––> Output: Scalen Triangle
def typeOfTRiangle(i, j, k):
    if i+j+k == 180 and i != j != k:
        return 'Scalene Triangle'
    elif i+j+k == 180 and i != j == k :
        return 'Isoceles Triangle'
    elif i+j+k == 180 and i == j == k:
        return 'Equilateral triangle'
    else:
        return 'Not a triangle'
# print(typeOfTRiangle(60,60,70))

#Nearest prime number
def check_prime(num):
    flag = 1 #prime
    for i in range(2, int(pow(num, 0.5))+1):
        if num % i == 0:
            flag = 0
            break
    if flag == 0:
        return False
    return True
# print(check_prime(22))

def nearest_prime(num, call):
    if check_prime(num):
        return [num, call]
    return nearest_prime(num-1, call+1)
# print(nearest_prime(10000))
ans = nearest_prime(10000, 0)
# print('nearest prime no. is : ', ans[0])
# print('no. of recursive calls : ', ans[1])
# print(id(ans))

#generate similar to dictionary using counter  
from collections import Counter
#frequency of no.
aray = [1,1,21,15,1,165,1,2,3,21,25,16,1]
c = Counter(aray)
# print(c, type(c))
# print(id(aray[0]), id(aray[-1])) #address location 
# print(id(aray))

# Given an array, your function should return the length of the array.
# Example:
# Input: arrayLength([1,5,3,7,8]) ––> Output: 5
def lengthArray(arr):
    # return len(a)
    count = 0
    for i in arr:
        count += 1
    return count
# print(lengthArray([1,5,3,7,8]))

# Given an array and an item, your function should return the index at which the item is present.
# Example:
# Input: indexOf([1,6,3,5,8,9], 3) ––> Output: 2
def indexOf(arr, n):
    for i in range(len(arr)):
        if arr[i] == n:
            return i
    return False
# print(indexOf([1,6,3,5,8,9], 3))

# Given an array and two numbers, your function should replace all entries of first number in an array with the second number.
# Example:
# Input: replace([1,5,3,5,6,8], 5, 10) ––> Output: [1,10,3,10,6,8]
def replace(arr, n, r):
    for i in range(len(arr)):
        if arr[i] == n:
            arr[i] = r
    return arr
# print(replace([1,5,3,5,6,8], 5, 10))

# Given two arrays, your function should return single merged array.
# Example:
# Input: mergeArray([1,3,5], [2,4,6]) ––> Output: [1,3,5,2,4,6]
def mergeArray(arr1, arr2):
    # arr = arr1+arr2
    # return arr
    arr1.extend(arr2)
    return arr1
# print(mergeArray([1,3,5], [2,4,6]))

# Given a string and an index, your function should return the character present at that index in the string.
# Example:
# Input: charAt("neoGcamp", 4) ––> Output: c
def charAt(s, i):
    return s[i]
# print(charAt("neoGcamp", 4))

# Given two dates, your function should return which one comes before the other.
# Example:
# Input: minDate('02/05/2021', '24/01/2021') ––> Output: 24/01/2021
def minDate(d1, d2):
    day1 = d1.split('/')
    day2 = d2.split('/')
    if int(day1[-1]) >= int(day2[-1]) and int(day1[1]) >= int(day2[1]) and int(day1[0]) >= int(day2[0]):
        return d1
    elif int(day1[-1]) >= int(day2[-1]) and int(day1[1]) >= int(day2[1]) and int(day1[0]) <= int(day2[0]):
        return d2
# print(minDate('02/05/2021', '24/01/2021')) #INCORRECT OR RECHECK AGAIN

# Write a function which generates a secret code from a given string, by shifting characters of alphabet by N places. Example:
# Input: encodeString("neogcamp", 2) ––> Output: pgqiecor
# Explanation: 2 represents shifting alphabets by 2 places. a –> c, b –> d, c –> e and so on.
def encodeString(s, p):
    d = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}
    val = ''
    for i in range(len(s)):
        for j in range(1, len(d)+1):
            if s[i] == d[j]: 
                val += d[j+p]
    return val        
# print(encodeString("neogcamp", 2))

# Given a sentence, return a sentence with first letter of all words as capital.
# Example:
# Input: toSentenceCase('we are neoGrammers') ––> Output: We Are NeoGrammers
def toSentenceCase(s):
    s = s.split(' ')
    val = ''
    for i in s:
        val += i.capitalize()+ ' '
    return val
# print(toSentenceCase('we are neoGrammers'))

# Given an array of numbers, your function should return an array in the ascending order.
# Example:
# Input: sortArray([100,83,32,9,45,61]) ––> Output: [9,32,45,61,83,100]
def sortArray(arr):
    arr.sort()
    return arr
# print(sortArray([100,83,32,9,45,61]))

# Given a sentence, your function should reverse the order of characters in each word, keeping same sequence of words.
# Example:
# Input: reverseCharactersOfWord('we are neoGrammers') –––> Output: ew era sremmarGoen
def reverseCharactersOfWord(s):
    s = s[::-1].split(' ')[::-1]
    res = ''
    for i in s:
        res += i + ' '
    return res
# print(reverseCharactersOfWord('we are neoGrammers'))

