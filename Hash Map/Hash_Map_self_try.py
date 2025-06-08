class HashMap:
    def __init__(self):
        self.size = 10
        self.map = [[] for _ in range(self.size)]

    def get_hash(self, key):
        return hash(key) % self.size

    def print_hash_map(self):
        for i in range(self.size):
            print(i, " : ", self.map[i])

    def add_values(self, key, value):
        h = self.get_hash(key=key)

        for pair in self.map[h]:
            if pair[0] == key:
                pair[1] = value
        self.map[h].append([key, value])

    def remove_values(self, key):
        h = self.get_hash(key=key)

        for i, pair in enumerate(self.map[h]):
            if pair[0] == key:
                del self.map[h][i]
                return True
            return False


if __name__ == "__main__":
    root = HashMap()

    # root.print_hash_map()

    root.add_values(key='key 1', value=5)
    root.add_values(key='key 2', value=10)
    root.add_values(key='key 3', value=15)

    root.print_hash_map()

    root.remove_values(key='key 2')

    root.print_hash_map()