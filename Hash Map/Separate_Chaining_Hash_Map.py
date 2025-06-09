
class HashMap:
    def __init__(self):
        self.size = 10
        self.map = [[] for _ in range(self.size)]

    def get_hash(self, key):
        return hash(key) % self.size

    def insert_value(self, key, value):
        h = self.get_hash(key=key)

        for pair in self.map[h]:
            if pair[0] == key:
                pair[1] = value

        self.map[h].append([key, value])

    def delete_value(self, key):
        h = self.get_hash(key=key)
        for i, pair in enumerate(self.map[h]):
            if pair[0] == key:
                del self.map[h][i]
                return True
            return False

    def print_hash_map(self):
        for i in range(self.size):
            print(i, " : ", self.map[i])

if __name__ == "__main__":
    root = HashMap()

    root.insert_value(key='key 1', value=5)
    root.insert_value(key='key 2', value=10)
    root.insert_value(key='key 3', value=15)
    root.insert_value(key='key 4', value=20)

    root.print_hash_map()
    print("\n")

    root.delete_value(key='key 3')

    root.print_hash_map()
    print("\n")