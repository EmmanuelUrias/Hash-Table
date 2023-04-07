class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    # def add(self, key, value):
    #     h = self.get_hash(key)
    #     self.arr[h] = value

    # built in python operator that allows us to get the add functionality with just square brackets
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False

        for index, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][index] - (key, value)
                found = True
                break
            if not found:
                self.arr[h].append((key, value))

    # def get(self, key):
    #     h = self.get_hash(key)
    #     return self.arr[h]

    # built in python operator that allows us to get an item by just putting the key within square brackets
    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]


t = HashTable()
# t.add('march 10', 205)
new_day = t['march 11'] = 212
new_day2 = t['march 11'] = 211
print(new_day)
print(new_day2)
print(t.get_hash('march 11'))
# print(t.add('march 11', 212))
# print(t['march 10'])
# print(t.get('march 10'))
# del t['march 10']
# print(t['march 10'])
print(t.arr)
