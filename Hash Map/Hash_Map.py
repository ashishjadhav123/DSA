
class HashMap:
    def __init__(self):
        self.size = 10
        self.map = [[] for _ in range(self.size)]

    def get_hash(self, key):
        return hash(key) % self.size

    def add(self, key, value):
        h = self.get_hash(key=key)

        for pair in self.map[h]:
            if pair[0] == key:
                pair[1] = value
                return
        self.map[h].append([key, value])

    def get(self, key):
        h = self.get_hash(key=key)

        for pair in self.map[h]:
            if pair[0] == key:
                return pair[1]

        return None


    def delete(self, key):

        h = self.get_hash(key=key)

        for i, pair in enumerate(self.map[h]):
            if pair[0] == key:
                del self.map[h][i]
                return True
        return False

    def print_hash_map(self):
        for i in range(self.size):
            print(i, " : ", self.map[i])

        print('\n')


if __name__ == "__main__":
    root = HashMap()

    root.add(key='key 1', value=5)
    root.add(key='key 2', value=10)
    root.add(key='key 3', value=15)
    root.add(key='key 4', value=20)
    root.add(key='key 5', value=25)
    root.add(key='key 6', value=30)

    root.print_hash_map()

    print(root.get(key='key 4'))

    root.delete(key='key 4')

    root.print_hash_map()