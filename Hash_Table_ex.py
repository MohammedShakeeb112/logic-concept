with open('/mnt/A4B278D5B278AD84/Python+ml Crash Course/pythonPracticeQuest/logic/nyc_weather.csv') as f:
    ls = list(f)[1:]
    dic = {}
    
    for line in ls:
        token = line.split(',')
        dic[token[0]] = (int(token[1].replace('\n','')))

# What was the average temperature in first week of Jan
# print(dic)
# avg = sum/len
def avgTempWeek():
    totalsum = 0
    count = 0
    for i,kv in enumerate(dic):
        if i < 7:
            totalsum += int(dic[kv])
            count += 1
    return round(totalsum /count, 2)
# print('Average Temperature on Week :', avgTempWeek())

# efficient way
with open('/mnt/A4B278D5B278AD84/Python+ml Crash Course/pythonPracticeQuest/logic/nyc_weather.csv') as f:
    arr = []
    for line in list(f)[1:]:
        token = line.split(',')
        arr.append(int(token[1].replace('\n','')))
# print(arr)
avg = sum(arr[:7])/len(arr[:7])
# print(avg)

def maxTemp():
    maxtemp = 0
    for i,kv in enumerate((dic)):
        maxtemp = max(maxtemp, int(dic[kv]))
    return maxtemp
# print('Max Temperature :',maxTemp())

# efficient way 
maxtemp = max(arr[:])
# print(maxtemp)

# What was the temperature on Jan 9?
# print('Temperature on Jan 9 :', dic['Jan 9'])
# What was the temperature on Jan 4?
# print('Temperature on Jan 4 :', dic['Jan 4'])

# poem.txt Contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in python and print every word and its count as show below. Think about the best data structure that you can use to solve this problem and figure out why you selected that specific data structure.
# 'diverged': 2,
#  'in': 3,
#  'I': 8
with open('/mnt/A4B278D5B278AD84/Python+ml Crash Course/pythonPracticeQuest/logic/poem.txt') as f:
    word_count = {}
    for line in f:
        tokens = line.split(' ')
        for token in tokens:
            word = token.replace('\n','').replace('—','')
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
# print(word_count)

# Implement hash table where collisions are handled using linear probing. We learnt about linear probing in the video tutorial. Take the hash table implementation that uses chaining and modify methods to use linear probing. Keep MAX size of arr in hashtable as 10.
class HashTable:
    def __init__(self):
        self.max = 10
        self.arr = [None for i in range(self.max)]

    def get_key(self, key):
        key_idx = 0
        for i in key:
            key_idx += ord(i)
        return key_idx % self.max

    def __setitem__(self, key, val):
        key_idx = self.get_key(key)
        if self.arr[key_idx] is None:
            self.arr[key_idx] = (key, val)
        else:
            new_idx = self.find_idx(key, key_idx)
            self.arr[new_idx] = (key, val)
        print(self.arr)
    
    def __getitem__(self, key):
        key_idx = self.get_key(key)
        if self.arr[key_idx] is None:
            return
        ranges = self.get_range(key_idx)
        for r in ranges:
            el = self.arr[r]
            if el is None:
                return
            if el[0] == key:
                return el[1]
        return False

    def __delitem__(self, key):
        key_idx = self.get_key(key)
        if self.arr[key_idx] is None:
            return
        if self.arr[key_idx][0] == key:
            self.arr[key_idx] = None
        r = self.find_idx(key, key_idx)
        if self.arr[r][0] == key:
            self.arr[r] = None
        print(self.arr)

    def find_idx(self, key, idx):
        ranges = self.get_range(idx)
        for r in ranges:
            if self.arr[r] is None:
                return r
            if self.arr[r][0] == key:
                return r
        raise Exception('List is Full')

    def get_range(self, idx):
        return [*range(idx, len(self.arr))] + [*range(idx)]

h = HashTable()
# print(h.get_range(9))
# h['march 6'] = 64
# h['march 17'] = 191
# print(h['march 17'])
# del h['march 17']
t = HashTable()
t["march 6"] = 20
t["march 17"] =  88
t["march 17"] = 29
t["nov 1"] = 1
t["march 33"] = 234
print('------->>>>', t["dec 1"])
print(t["march 33"])
t["march 33"] = 999
print(t["march 33"])
t["april 1"]=87
t["april 2"]=123
t["april 3"]=234234
t["april 4"]=91
t["May 22"]=4
t["May 7"]=47
# t["Jan 1"]=0 #throw exception 
del t["april 2"]
t["Jan 1"]=0
print('------->>>>', t["dec 1"])
print(h.get_key('dec 1'))