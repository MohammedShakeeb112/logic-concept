#Queue => FIFO => FIRST-IN-FIRST-OUT
#Stock exchange is best example every minute SE produces different price for an entity,
#so that consumer entity will consume it for every minute

# ++++++++++++++QUEUE USING LIST+++++++++++++++++++
queue = []
queue.insert(0, 131.10) # @ 10:25am price
queue.insert(0, 128.50) # @ 10:26am price
queue.insert(0, 165.21) # @ 10:27am price
# print(queue)
# print(queue.pop())
# print(queue.pop())
# print(queue.pop())
# print(queue.pop()) # throw error list got emptied
# print(queue)

# ++++++++++++++++++QUEUE USING DEQUE++++++++++++++
from collections import deque
queue = deque()
# print(queue)
queue.appendleft(121.15)
queue.appendleft(216.25)
queue.appendleft(391.38)
# print(queue)
# print(queue.pop())
# print(queue.pop())
# print(queue.pop())
# print(queue.pop()) #emptied error in deque
# print(queue)

# +++++++++++++++QUEUE USING OOPS+++++++++++++++++
class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, d):
        self.queue.insert(0, d)

    def dequeue(self):
        if self.size() <= 0:
            return ('Empty List')
        else:
            return self.queue.pop()

    def peek(self):
        return self.queue[-1]

    def size(self):
        count = 0
        for i in self.queue:
            count += 1
        return count

    def print(self):
        print(self.queue)

q = Queue()
# q.enqueue(121.15)
# q.enqueue(216.25)
# q.enqueue(391.38)
# q.print()
# print(q.size())
# print(q.peek())
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.print()
# print(q.size())
q.enqueue({
    'company': 'IKEA',
    'timestamp':'12 March, 10:15 AM',
    'price': 121.15
})
q.enqueue({
    'company': 'IKEA',
    'timestamp':'12 March, 10:16 AM',
    'price': 216.25
})
q.enqueue({
    'company': 'IKEA',
    'timestamp':'12 March, 10:17 AM',
    'price': 391.38
})
# q.print()
# print(q.size())
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())
# q.print()
# print(q.size())

# ++++++++++++++++++QUEUE EXERCISE+++++++++++++++++++++
# Design a food ordering system where your python program will run two threads,
#     Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
#     Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.
# Use this video to get yourself familiar with multithreading in python
# Pass following list as an argument to place order thread,
# orders = ['pizza','samosa','pasta','biryani','burger']

import time, threading
class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, d):
        self.queue.appendleft(d)

    def dequeue(self):
        if self.length() <= 0:
            return 'Empty List'
        return self.queue.pop()

    def peek(self):
        if self.length() <= 0:
            return 'Empty List'
        return self.queue[-1]

    def length(self):
        return len(self.queue)

food_order = Queue()

def place_order(orders):
    for order in orders:
        food_order.enqueue(order)
        print('PLACING ORDER', order)
        time.sleep(0.5)

def serve_order():
    time.sleep(1)
    i = 6
    while i:
        order = food_order.dequeue()
        print('SERVING ORDER', order)
        time.sleep(2)
        i -= 1
# if __name__ == '__main__':
#     orders = ['pizza','samosa','pasta','biryani','burger']
#     t1 = threading.Thread(target=place_order, args=(orders,))
#     t2 = threading.Thread(target=serve_order)
#     t1.start()
#     t2.start()


# Write a program to print binary numbers from 1 to 10 using Queue. Use Queue class implemented in main tutorial. Binary sequence should look like,
# 1
# 10
# 11
# 100
# 101
# 110
# 111
# 1000
# 1001
# 1010
# Hint: Notice a pattern above. After 1 second and third number is 1+0 and 1+1. 4th and 5th number are second number (i.e. 10) + 0 and second number (i.e. 10) + 1.
# You also need to add front() function in queue class that can return the front element in the queue.
def binNum(num):
    while num <= 10:
        print(bin(num)[2:])
        num += 1
# binNum(1)

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, d):
        self.queue.appendleft(d)

    def dequeue(self):
        if self.length() <= 0:
            return 'Empty List'
        return self.queue.pop()

    def peek(self):
        if self.length() <= 0:
            return 'Empty List'
        return self.queue[-1]

    def length(self):
        return len(self.queue)

def produce_bin(n):
    q = Queue()
    q.enqueue('1')
    for i in range(n):
        peek = q.peek()
        print(peek)
        q.enqueue(peek+'0')
        q.enqueue(peek+'1')
        q.dequeue()
# if __name__ == '__main__':
#     produce_bin(10)