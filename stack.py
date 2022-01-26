#stack usecase => browser history are stored in the stack LIFO (LAST-IN-FIRST-OUT)
#operation in stack => push, peek, pop
# +++++++++++++++++++++++USING LIST++++++++++++++++++++++++++++++++++
# print(dir(list))
stack = []
stack.append(4)
stack.append(3)
stack.append(2)
stack.append(1)
# print(stack)
stack.pop()
# print(stack)
# print(stack.count(2))
stack.pop()
stack.pop()
stack.pop()
# stack.pop() #throw error empty list
# print(stack)

#++++++++++++++++USING DEQUE++++++++++++++++++++
from collections import deque
stack = deque()
# print(dir(stack))
# print(stack)
stack.append(4)
stack.append(3)
stack.append(2)
stack.append(1)
# print(stack)
stack.pop()
# print(stack)
stack.pop()
stack.pop()
stack.pop()
# stack.pop() #throw empty deque error
# print(stack)

# +++++++++++++++++USING CLASS & DEQUE+++++++++++++++
class Stack:
    def __init__(self):
        self.stack = deque()

    def add(self, d):
        self.stack.append(d)
        # print(self.stack)

    def delete(self):
        if self.length() <= 0:
            print('Empty Stack')
        else:
            return self.stack.pop()
            # print(self.stack)
        
    def peek(self):
        print(self.stack[-1])

    def length(self):
        # count = 0
        # for i in self.stack:
        #     count += 1
        # return count
        return len(self.stack)

    def print(self):
        print(self.stack)

s = Stack()
# s.add(4)    
# s.add(3)    
# s.add(2)    
# s.add(1)    
# s.peek()
# s.delete()
# s.print()
# s.delete()
# s.delete()
# s.delete()
# s.delete()
# s.print()
# print(s.length())


#++++++++++++++++++++++++++++EXCERCISE+++++++++++++++++++++++
# Write a function in python that can reverse a string using stack data structure. Use Stack class from the tutorial.
# reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"
class ReverseString:
    def __init__(self):
        self.rs = deque()

    def push(self, d):
        self.rs.append(d)

    def rev_str(self):
        return self.rs[0][::-1]

    def print(self):
        print(self.rs)

rs = ReverseString()
rs.push("We will conquere COVID-19")
# rs.print()
# print(rs.rev_str())

#efficient way
def reverse_string(s):
    stack = Stack()
    for l in s:
        stack.add(l)
    rs = ''
    while stack.length():
        rs += stack.delete()
    return rs
# print(reverse_string("We will conquere COVID-19"))

# Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial.
# is_balanced("({a+b})")     --> True
# is_balanced("))((a+b}{")   --> False
# is_balanced("((a+b))")     --> True
# is_balanced("))")          --> False
# is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True
def check(c1, c2):
    d = {')':'(', '}':'{', ']':'['}
    return d[c1] == c2

def Parenthesis(s):
    stack = Stack()
    for l in s:
        if l == '(' or l == '{' or l == '[':
            stack.add(l)
        if l == ')' or l == '}' or l == ']':
            if stack.length() == 0:
                return False
            if not check(l, stack.delete()):
                return False
    return stack.length() == 0

print(Parenthesis('({a+b})'))
print(Parenthesis('))((a+b}{'))
print(Parenthesis('((a+b))'))
print(Parenthesis('))'))
print(Parenthesis('[a+b]*(x+2y)*{gg+kk}'))