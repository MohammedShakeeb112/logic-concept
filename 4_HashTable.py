stock = []
with open('/mnt/A4B278D5B278AD84/Python+ml Crash Course/pythonPracticeQuest/logic/stock_prices.csv') as f:
    for line in f:
        token = line.split(',')
        day = token[0]
        price = float(token[1])
        stock.append([day, price])
# print(stock)

# Find stock price on March 9
# for e in stock:  # Complexity of search using a list is O(n)
#     if e[0] == 'march 9':
#         print(e[1])


# Process using python dictionary
dic = {}
with open('/mnt/A4B278D5B278AD84/Python+ml Crash Course/pythonPracticeQuest/logic/stock_prices.csv') as f:
    for line in f:
        token = line.split(',')
        day = token[0]
        price = float(token[1])
        dic[day] = price
# print(dic)
# print(dic['march 9'])   # Complexity of search using dictionary is O(1)


# Implement Hash Table
def get_hash(key):
    hash = 0
    for i in key:
        hash += ord(i)
    return hash % 100
# print(get_hash('march 9'))
capltr = {}
for i in range(65,91):
    capltr[i] = chr(i)
smlltr = {}
for i in range(97,123):
    smlltr[i] = chr(i)
num = {}
for i in range(48, 58):
    num[i] = chr(i)
# print(capltr)
# print(smlltr)
# print(num)

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [0 for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for i in key:
            hash += ord(i)
        return hash % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val
        return self.arr

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        del self.arr[h]
# for i in range(97,97+26):
#     print(i, chr(i))
h = HashTable()
h.get_hash('march 30')
h.get_hash('dec 4')
# h.add('dec 4', 263)
# print(h.arr)
# print(h.get('dec 4'))
# print(h['dec 4'])
h['dec 4'] = 231
h['jan 23'] = 96
h['february 3'] = 619
h['mango'] = 21
# print(h.arr)
del h['mango']
# print(h.arr)

# --------------------4_hash_table_collision_handling--------------------------
class Hash:
    def __init__(self):
        self.max = 10
        self.arr = [0 for i in range(self.max)]

    def get_hash(self, key):
        hash = 0
        for i in key:
            hash += ord(i)
        return hash % self.max

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        del self.arr[h]

h = Hash()
# print(h.get_hash('mango 50'))
# h['mango 59'] = 62
# print(h['mango 59'])
# del h['mango 59']
# print(h.arr)
# print(h.get_hash('march 6'))  #march 6, march 17 having same index
# print(h.get_hash('march 17'))
# print(h.get_hash('march 8'))
# print(h.get_hash('march 9'))
h['march 6'] = 49
h['march 17'] = 610
h['march 8'] = 261
h['march 9'] = 513
# print(h['march 6'])
# print(h.arr)

# Hash Table Collision Handling Using Chaining====>
class Hash_table:
    def __init__(self):
        self.max = 10
        self.arr = [[] for i in range(self.max)]

    def gethash(self, key):
        hash = 0
        for i in key:
            hash += ord(i)
        return hash % self.max

    def __setitem__(self, key, val):
        h = self.gethash(key)
        found = False
        for idx, ele in enumerate(self.arr[h]):
            if len(ele) == 2 and ele[0] == key:
                self.arr[h][idx] = (key, val) 
                found = True
        if not found:
            self.arr[h].append((key, val))
    
    def __getitem__(self, key):
        arr_index = self.gethash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]
        return False

    def __delitem__(self, key):
        arr_index = self.gethash(key)
        for idx, kv in enumerate(self.arr[arr_index]):
            if len(kv) == 2 and kv[0] == key:
                print('delete', idx)
                del self.arr[arr_index][idx]

ht = Hash_table()
ht["march 6"] = 310
ht["march 7"] = 420
ht["march 8"] = 67
ht["march 17"] = 63457
print(ht.arr)
ht['march 7'] = 313
print(ht.arr)
del ht['march 17']