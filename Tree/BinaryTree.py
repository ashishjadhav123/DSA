

class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert_node(self, data):
        """ Insert Node in Binary Tree"""
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
        """ in_Order Traversal in Binary Tree"""
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

    def search(self, val):
        """ Search value in Binary Tree"""
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val=val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val=val)
            else:
                return False

    def delete_node(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete_node(val=val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete_node(val=val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete_node(val=min_val)

        return self

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()


def build_tree(elements):
    """ Method to create Binary Tree from a List """
    root = BinarySearchTree(data=elements[0])

    for i in range(1, len(elements)):
        root.insert_node(data=elements[i])

    return root


if __name__ == "__main__":
    numbers = [10, 6, 12, 3, 15, 8, 17, 11]
    tree = build_tree(elements=numbers)


    print(tree.search(val=8))
    print(tree.search(val=26))

    print(tree.in_order_traversal())

    tree.delete_node(val=11)

    print(tree.in_order_traversal())

    pass
