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

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)


hash_table = HashTable()
hash_table.set_item("name", "steven")
hash_table.print_table()
print(hash_table.get_item("name"))
