
class DNode:
    def __init__(self, data=None, prv=None, next=None):
        self.data = data
        self.prv = prv
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """Method to insert element at beginning of Linked List"""
        node = DNode(data=data, next=self.head)

        if self.head is not None:
            self.head.prv = node

        self.head = node

    def print_linked_list(self):
        """Method for print all elements from Linked List"""
        itr = self.head

        l_list_str = ""

        while itr:
            suffix = ""
            if itr.next:
                suffix = " ⇄ "
            l_list_str += str(itr.data) + suffix
            itr = itr.next
        return l_list_str

    def get_length_linked_list(self):
        """Method for get length of Linked List"""
        itr = self.head
        counter = 0

        while itr:
            counter += 1
            itr = itr.next

        return counter


    def insert_at_end(self, data):
        """Method to insert element at end of Linked List"""
        if self.head is None:
            self.head = DNode(data=data, next=self.head, prv=None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = DNode(data=data, prv=itr)

    def insert_at_loc(self, index, data):
        """Method to insert element at specific index of Linked List"""
        if index < 0 or index > self.get_length_linked_list():
            raise Exception("Enter valid Index")

        if index == 0:
            self.insert_at_beginning(data=data)
            return

        itr = self.head
        counter = 0

        while itr:
            if counter == (index - 1):
                itr.next = DNode(data=data, next=itr.next)
                break
            counter += 1
            itr = itr.next

    def remove_by_index(self, index):
        """Method to remove element at specific index of Linked List"""
        if index < 0 or index > self.get_length_linked_list():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next

        itr = self.head
        counter = 0

        while itr:
            if counter == (index - 1):
                itr.next = itr.next.next
                break
            itr = itr.next
            counter += 1

    def remove_by_value(self, data):
        """Method to Remove before element Linked List"""
        if self.head == None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head

        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next
        else:
            print("Data not found")


if __name__ == '__main__':
    root = DoublyLinkedList()

    root.insert_at_beginning(5)
    root.insert_at_beginning(10)

    print(root.print_linked_list())
    print(f"Length of our Linked List is {root.get_length_linked_list()}.")

    root.insert_at_end(15)
    root.insert_at_end(20)

    print(root.print_linked_list())
    print(f"Length of our Linked List is {root.get_length_linked_list()}.")

    root.insert_at_loc(index=2, data=35)
    root.insert_at_loc(index=0, data=45)

    print(root.print_linked_list())
    print(f"Length of our Linked List is {root.get_length_linked_list()}.")

    root.remove_by_index(2)
    root.remove_by_index(0)

    print(root.print_linked_list())
    print(f"Length of our Linked List is {root.get_length_linked_list()}.")

    root.remove_by_value(20)

    print(root.print_linked_list())
    print(f"Length of our Linked List is {root.get_length_linked_list()}.")