
class BinartTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_node(self, data):
        if self.data == data:
            return

        if data < self.data:
            if self.left:
                self.left.add_node(data=data)
            else:
                self.left = BinartTree(data=data)

        else:
            if self.right:
                self.right.add_node(data=data)
            else:
                self.right = BinartTree(data=data)

    def in_order_traversal(self):
        elements = []

        if self.left:
            left_elements = self.left.in_order_traversal()
            elements += left_elements

        elements.append(self.data)

        if self.right:
            right_elements = self.right.in_order_traversal()
            elements += right_elements

        return elements

    def search_node(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search_node(val=val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search_node(val=val)
            else:
                return False


def build_tree(elements):
    root = BinartTree(elements[0])

    for i in range(1, len(elements)):
        root.add_node(data=elements[i])

    return root


if __name__ == "__main__":
    numbers = [10, 5, 12, 16, 3, 9, 11, 2, 19]

    tree = build_tree(elements=numbers)

    print(tree.in_order_traversal())

    print(tree.search_node(val=9))
    print(tree.search_node(val=22))