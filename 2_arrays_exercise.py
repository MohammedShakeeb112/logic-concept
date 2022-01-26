# Exercise: Array DataStructure

#     Let us say your expense for every month are listed below,
#         January - 2200
#         February - 2350
#         March - 2600
#         April - 2130
#         May - 2190

# Create a list to store these monthly expenses and using that find out,

# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

monthly_Expenses = [2200, 2350, 2600, 2130, 2190]
febXtraThanJan = monthly_Expenses[1] - monthly_Expenses[0]
# print(febXtraThanJan)
totalExp = sum(monthly_Expenses[:3])
# print(totalExp)
def exSp(es):
    for i in monthly_Expenses:
        if i == es:
            return True
    return False
# print(exSp(2000))
monthly_Expenses.append(1980)
# print(monthly_Expenses)
monthly_Expenses[3] -= 200
# print(monthly_Expenses)


# You have a list of your favourite marvel super heros.
# heros=['spider man','thor','hulk','iron man','captain america']
# Using this find out,
# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros=['spider man','thor','hulk','iron man','captain america']
# print(len(heros))
def length(lis):
    count = 0
    for i in lis:
        count += 1
    return count
# print(length(heros))
heros.append('black panther')
# print(heros)
heros.remove('black panther')
# print(heros)
heros.insert(3, 'black panther')
# print(heros)
# for i in range(len(heros)):
#     if heros[i] == 'thor' or heros[i] == 'hulk':
#         heros[i] = 'doctor strange'
# print(heros)
heros[1:3]=['doctor strange']
# print(heros)
heros.sort()
# print(heros)

# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
n = int(input('enter the no. '))
def odd_max(n):
    result = [i for i in range(1,n) if i%2 != 0]
    return result
# print(odd_max(n))