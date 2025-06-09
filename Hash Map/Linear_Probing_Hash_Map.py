
class HashMap:
    def __init__(self):
        self.size = 10
        self.hash = [None] * self.size

    def get_hash(self, key):
        return hash(key) % self.size

    def insert_value(self, key, value):
        idx = self.get_hash(key=key)
        original_idx = idx

        while self.hash[idx] is not None:
            if self.hash[idx][0] == key:
                self.hash[idx] = (key, value)
                return
            idx = (idx + 1) % self.size
            if idx == original_idx:
                raise Exception("HashMap is full")
        self.hash[idx] = (key, value)

    def delete_val(self, key):
        idx = self.get_hash(key=key)

        while self.hash[idx] is not None:
            if self.hash[idx][0] == key:
                self.hash[idx] = [None]
                return
            else:
                print(f"{key} is not present in HashMap")
                return


    def print_hash_map(self):
        for i in range(self.size):
            print(i, " : ", self.hash[i])


if __name__ == "__main__":
    root = HashMap()

    root.insert_value(key='key 1', value=5)
    root.insert_value(key='key 2', value=10)
    root.insert_value(key='key 3', value=15)
    root.insert_value(key='key 4', value=20)
    root.insert_value(key='key 5', value=25)
    root.insert_value(key='key 6', value=30)
    root.insert_value(key='key 7', value=35)
    root.insert_value(key='key 8', value=40)
    root.insert_value(key='key 9', value=45)
    root.insert_value(key='key 10', value=50)
    # root.insert_value(key='key 11', value=55)

    root.print_hash_map()
    print('\n')

    root.delete_val(key='key 5')
    root.delete_val(key='key 3')
    root.delete_val(key='key 5')

    root.print_hash_map()

