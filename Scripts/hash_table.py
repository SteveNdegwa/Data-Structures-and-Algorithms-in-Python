class HashTable(object):
    def __init__(self, size=7):
        self.data_map = [None] * size

    def hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def set_item(self, key, value):
        index = self.hash(key)
        if not self.data_map[index]:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.hash(key)
        if self.data_map[index]:
            for i, value in enumerate(self.data_map[index]):
                if value[0] == key:
                    return value[1]
        return None

    def keys(self):
        keys_list = []
        for i in range(len(self.data_map)):
            if self.data_map[i]:
                for j in range(len(self.data_map[i])):
                    keys_list.append(self.data_map[i][j][0])
        return keys_list

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)


hash_table = HashTable()
hash_table.set_item("name", "steven")
hash_table.set_item("age", "12")
hash_table.set_item("position", "manager")
hash_table.print_table()
print(hash_table.get_item("name"))
print(hash_table.keys())
