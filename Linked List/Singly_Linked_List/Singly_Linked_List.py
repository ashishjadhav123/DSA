
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """Method to insert element at beginning of Linked List"""
        node = Node(data=data, next=self.head)
        self.head = node

    def print_l_list(self):
        """Method for print all elements from Linked List"""
        itr = self.head
        l_list_str = ''

        while itr:
            suffix = ''
            if itr.next:
                suffix = '-->'
            l_list_str += str(itr.data) + suffix
            itr = itr.next

        print(l_list_str)

    def get_length(self):
        """Method for get length of Linked List"""
        counter = 0
        itr = self.head
        while itr:
            counter += 1
            itr = itr.next

        # print(f"Length of our Linked List is {counter}.")
        return counter

    def insert_at_end(self, data):
        """Method to insert element at end of Linked List"""
        if data is None:
            return

        if self.head is None:
            self.head = Node(data=data, next=None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data=data)

    def insert_at_loc(self, index, data):
        """Method to insert element at specific index of Linked List"""
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_beginning(data=data)
            return

        itr = self.head
        counter = 0
        while itr:
            if counter == index - 1:
                node = Node(data=data, next=itr.next)
                itr.next = node
                break

            itr = itr.next
            counter += 1

    def remove_at_loc(self, index):
        """Method to remove element at specific index of Linked List"""
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return

        itr = self.head
        counter = 0
        while itr:
            if counter == index -1:
                itr.next = itr.next.next
                break

            itr = itr.next
            counter += 1


if __name__ == '__main__':
    root = SinglyLinkedList()

    root.insert_at_beginning(data=5)
    root.insert_at_beginning(data=10)
    root.insert_at_beginning(data=15)

    root.print_l_list()
    print(f"Length of our Linked List is {root.get_length()}.")

    root.insert_at_end(data=20)
    root.insert_at_end(data=25)
    root.insert_at_end(data=30)

    root.print_l_list()
    print(f"Length of our Linked List is {root.get_length()}.")

    root.insert_at_loc(index=3, data=100)
    root.print_l_list()
    print(f"Length of our Linked List is {root.get_length()}.")
    root.insert_at_loc(index=1, data=200)
    root.print_l_list()
    print(f"Length of our Linked List is {root.get_length()}.")

    root.remove_at_loc(index=1)
    root.print_l_list()
    print(f"Length of our Linked List is {root.get_length()}.")

    root.remove_at_loc(index=6)
    root.print_l_list()
    print(f"Length of our Linked List is {root.get_length()}.")