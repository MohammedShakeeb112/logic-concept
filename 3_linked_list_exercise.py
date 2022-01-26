# Exercise: Linked List

#     In LinkedList class that we implemented in our tutorial add following two methods,

# def insert_after_value(self, data_after, data_to_insert):
#     # Search for first occurance of data_after value in linked list
#     # Now insert data_to_insert after data_after node

# def remove_by_value(self, data):
#     # Remove first node that contains data

# Now make following calls,

#     ll = LinkedList()
#     ll.insert_values(["banana","mango","grapes","orange"])
#     ll.print()
#     ll.insert_after_value("mango","apple") # insert apple after mango
#     ll.print()
#     ll.remove_by_value("orange") # remove orange from linked list
#     ll.print()
#     ll.remove_by_value("figs")
#     ll.print()
#     ll.remove_by_value("banana")
#     ll.remove_by_value("mango")
#     ll.remove_by_value("apple")
#     ll.remove_by_value("grapes")
#     ll.print()

class Node:
    def __init__(self, d, n=None):
        self.data = d
        self.next = n

class Linkedlist:
    def __init__(self):
        self.root = None

    def print(self):
        if self.root is None:
            print('Empty list')
            return
        cur_node = self.root
        lstr = ''
        while cur_node:
            lstr += str(cur_node.data) + '->' if cur_node.next else str(cur_node.data)
            cur_node = cur_node.next
        print(lstr)

    def get_length(self):
        cur_node = self.root
        count = 0
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def insert_at_begining(self, d):
        node = Node(d, self.root)
        self.root = node

    def insert_at_end(self, d):
        if self.root is None:
            self.insert_at_begining(d)
            return
        cur_node = self.root
        while cur_node.next != None:
            cur_node = cur_node.next
        cur_node.next = Node(d, cur_node.next)

    def insert_at(self, i, d):
        if i < 0 or i >= self.get_length(): 
            print('Invalid index')
            return
        if i == 0: 
            self.insert_at_begining(d)
            return
        cur_node = self.root
        count = 0
        while cur_node:
            if count == i - 1:
                cur_node.next = Node(d, cur_node.next)
            cur_node = cur_node.next
            count += 1

    def remove_at(self, i, d):
        if i < 0 or i >= self.get_length(): 
            print('Invalid index')
            return    
        if i == 0:
            self.root = self.root.next
            return
        count = 0
        cur_node = self.root
        while cur_node:
            if count == i - 1:
                cur_node.next = cur_node.next
                break
            cur_node = cur_node.next
            count += 1

    def insert_datalist(self, datalist):
        self.root = None
        for data in datalist:
            self.insert_at_end(data)

    def insert_after_value(self, val, d):
        if self.root is None:
            return 
        if self.root.data == val:
            self.root.next = Node(d, self.root.next)
            return

        cur_node = self.root
        while cur_node:
            if cur_node.data == val:
                cur_node.next = Node(d, cur_node.next)
                break
            cur_node = cur_node.next

    def remove_by_value(self, d):
        if self.root is None: return
        if self.root.data == d:
            self.root = self.root.next
            return

        cur_node = self.root
        while cur_node.next:
            if cur_node.next.data == d:
                cur_node.next = cur_node.next.next
                return True
            cur_node = cur_node.next
        return False

# if __name__ == '__main__':
#     ll = Linkedlist()
#     ll.insert_datalist(["banana","mango","grapes","orange"])
#     ll.print()
#     ll.insert_after_value("mango","apple") # insert apple after mango
#     ll.print()
#     ll.remove_by_value("orange") # remove orange from linked list
#     ll.print()
#     ll.remove_by_value("figs")
#     ll.print()
#     ll.remove_by_value("banana")
#     ll.remove_by_value("mango")
#     ll.remove_by_value("apple")
#     ll.remove_by_value("grapes")
#     ll.print()

#     ll.insert_datalist([45,7,12,567,99])
#     ll.insert_at_end(67)
#     ll.print()