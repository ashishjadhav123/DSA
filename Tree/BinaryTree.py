

class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert_node(self, data):
        if self.data == data:
            return

        if data < self.data:
            if self.left:
                self.left.insert_node(data=data)
            else:
                self.left = BinarySearchTree(data=data)

        else:
            if self.right:
                self.right.insert_node(data=data)
            else:
                self.right = BinarySearchTree(data=data)

    def in_order_traversal(self):
        elements = []

        # Insert Left nodes
        if self.left:
            left_elements = self.left.in_order_traversal()
            elements += left_elements

        elements.append(self.data)

        # Insert Right nodes
        if self.right:
            right_elements = self.right.in_order_traversal()
            elements += right_elements

        return elements


def build_tree(elements):

    root = BinarySearchTree(data=elements[0])

    for i in range(1, len(elements)):
        root.insert_node(data=elements[i])

    return root


if __name__ == "__main__":
    numbers = [10, 6, 12, 3, 15, 8, 17, 11]
    tree = build_tree(elements=numbers)

    print(tree.in_order_traversal())
    pass
