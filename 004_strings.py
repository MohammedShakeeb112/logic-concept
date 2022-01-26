# Write a program that converts the string into uppercase
def strUp(s):
    res = s.upper()
    return res
# print(strUp('uppercase'))

# Write a program that reads two strings and append first string to the second. So if first string is Good second string is Morning , the program should print MorningGood
def mergeStr(s1, s2):
    return s2+s1
# print(mergeStr('Good', 'Morning'))

# Program that reads string and count number of characters present in the string
def countStr(s):
    count = 1
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = count
    return d
# print(countStr('helloworld'))

# Write a program that converts string like "124" to 124
def strInt(s):
    return int(s)
# print(strInt('124'))

# Write a program to delete all vowels from a string. Assume string is not more than 80 characters long
def removeVowel(s):
    return s.translate({ord(i): None for i in 'aeiou'})
# print(removeVowel('hello world'))    

# Write a program to check whether the string is alphanumeric or not , eg:batman@45 contains digit 45
def alphnum(s):
    return s.isalnum()
# print(alphnum('batman45'))
# print(alphnum('batman@45'))

# A program that reads three strings and prints the longest and smallest one
def threeStr(s1, s2, s3):
    if len(s1) > len(s2) and len(s1) > len(s3):
        return s1
    elif len(s1) < len(s2) and len(s2) > len(s3):
        return s2
    return s3
# print(threeStr('tommorow land', 'hello world', 'welcoem'))

# Reverse the given string word wise. That is, the last word in given string should come at 1st place, last second word at 2nd place and so on. Individual words should remain as it is. example: Input : Welcome to NeoG Camp → Camp NeoG to Welcome
def revStrWord(s):
    res = ''
    for i in s.split()[::-1]:
        res += i + ' '  
    return res      
# print(revStrWord('Welcome to NeoG Camp'))

# Write a program to toggle case of each character of the string "good afternoon" (example: "neogcamp" ⇒ "nEoGcAmP" )
def toggleStr(s):
    res = ''
    for i in range(len(s)):
        if i % 2 == 0:
            res += s[i]
        else:
            res += s[i].upper()
    return res
# print(toggleStr('neogcamp'))

# Write a program which receives a string str that calculates the length of a string and return true if the length is greater than 7 without using strlen()
def strlen(s):
    count = 0
    for i in s:
        count += 1
    return count
# print(strlen('hello world'))

# Write a program that takes two strings and copies smaller string into bigger string
def smallbig(s1, s2):
    if len(s1) > len(s2):
        return ''+s1+s2
    else:
        return ''+s2+s1
# print(smallbig('hello', 'welcome'))

# Given a string, determine if it is a palindrome, considering only alphanumeric characters
def palindrome(s):
    org = s
    revs = s[::-1]
    if org == revs:
        return True
    return False
# print(palindrome('abcba'))
# print(palindrome('abca'))

def subStr(s):
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            print(s[i:j])
# subStr('abcd')

# Write a program that removes the time from the given date string "Wed April 15, 7pm". It should return only the date without the time.
def removeTime(s):
    res = s.split(',')[0]
    return res
# print(removeTime("Wed April 15, 7pm"))

# Write a program that masks all but last four characters of the string "5565534276455423" to '#'
def masks(s):
    res = ''
    if not res:
        res += s[:-4]
    for j in s[-4:]:
        res += str(j).replace(str(j), '#')
    return res
# print(masks("5565534276455423"))

# Given a string "tic tac toe is a fun game" convert the first 6 characters to capital case
def char6(s):
    return s[:6].upper()+s[6:]
# print(char6("tic tac toe is a fun game"))

# Given an input string S and two characters c1 and c2, you need to replace every occurrence of character c1 with character c2 in the given string
def replaceChar(s, c1, c2):
    res = s.replace(c1,c2)
    return res
# print(replaceChar('hetto wortd', 't', 'l'))

# Given an input string S that contains multiple words, you need to remove all the spaces present in the input string. There can be multiple spaces present after any word
def removeSpaces(s):
    res = s.replace(' ', '')
    return res
# print(removeSpaces('how are you nowdays'))

ASCII_SIZE = 256
def getMaxOccuringChar(str):
    # Create array to keep the count of individual characters
    # Initialize the count array to zero
    count = [0] * ASCII_SIZE
 
    # Utility variables
    max = -1
    c = ''
 
    # Traversing through the string and maintaining the count of
    # each character
    for i in str:
        count[ord(i)]+=1
 
    for i in str:
        if max < count[ord(i)]:
            max = count[ord(i)]
            c = i
 
    return c
 
# Driver program to test the above function
str = "sample string"
# print("Max occurring character is " + getMaxOccuringChar(str))

# Given a string "how was your day?" and a word "how", write a program that removes the occurrence of the specified word from given sentence. ( input: string⇒"programming camp are amazing",word⇒ "programming"; output:" camp are amazing")
def occRemove(s):
    return s.replace('programming ','')
# print(occRemove("programming camp are amazing"))