
class BinaryTree:
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
                self.left = BinaryTree(data=data)

        else:
            if self.right:
                self.right.insert_node(data=data)
            else:
                self.right = BinaryTree(data=data)

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


def build_tree(elements):
    root = BinaryTree(elements[0])

    for i in range(1, len(elements)):
        root.insert_node(data=elements[i])

    return root


if __name__ == "__main__":
    numbers = [10, 14, 4, 6, 19, 1, 7, 17, 20, 9]

    tree = build_tree(elements=numbers)

    print(tree.in_order_traversal())
