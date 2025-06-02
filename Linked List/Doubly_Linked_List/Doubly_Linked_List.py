
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
                d_node = DNode(data=data, next=itr.next, prv=itr)
                if itr.next:
                    itr.next.prev = d_node
                itr.next = d_node
                break
            counter += 1
            itr = itr.next

    def remove_by_index(self, index):
        """Method to remove element at specific index of Linked List"""
        if index < 0 or index > self.get_length_linked_list():
            raise Exception("Invalid Index")

        if index == 0:
            if self.head.next:
                self.head = self.head.next
                self.head.prv = None
            else:
                self.head = None
            return

        itr = self.head
        counter = 0

        while itr:
            if counter == index:
                if itr.prv:
                    itr.prv.next = itr.next
                if itr.next:
                    itr.next.prv = itr.prv
                break
            itr = itr.next
            counter += 1

    def remove_by_value(self, data):
        """Method to Remove before element Linked List"""
        if self.head is None:
            return

        if self.head.data == data:
            if self.head.next:
                self.head = self.head.next
                self.head.prv = None
            else:
                self.head = None
            return

        itr = self.head

        while itr:
            if itr.data == data:
                if itr.prv:
                    itr.prv.next = itr.next
                if itr.next:
                    itr.next.prv = itr.prv
                break

            itr = itr.next
        else:
            print(f"{data} not found in Linked List")


    def reverse_l_list(self):
        if self.head is None:
            return 'Empty Linked List'

        itr = self.head

        while itr.next:
            itr = itr.next

        reverse_str = ''
        while itr:
            suffix = " ⇄ " if itr.prv else ''
            reverse_str += str(itr.data) + suffix
            itr = itr.prv

        return reverse_str


if __name__ == '__main__':
    root = DoublyLinkedList()

    root.insert_at_beginning(5)
    root.insert_at_beginning(10)

    print(root.print_linked_list())
    print(f"Length of our Linked List is {root.get_length_linked_list()}.")
    print(root.reverse_l_list(), "\n")

    root.insert_at_end(15)
    root.insert_at_end(20)

    print(root.print_linked_list())
    print(f"Length of our Linked List is {root.get_length_linked_list()}.")
    print(root.reverse_l_list(), "\n")

    root.insert_at_loc(index=2, data=35)
    root.insert_at_loc(index=0, data=45)
    root.insert_at_loc(index=6, data=50)

    print(root.print_linked_list())
    print(f"Length of our Linked List is {root.get_length_linked_list()}.")
    print(root.reverse_l_list(), "\n")

    root.remove_by_index(2)
    # root.remove_by_index(0)

    print(root.print_linked_list())
    print(f"Length of our Linked List is {root.get_length_linked_list()}.")
    print(root.reverse_l_list(), "\n")

    # root.remove_by_value(45)
    root.remove_by_value(35)
    root.remove_by_value(35)

    print(root.print_linked_list())
    print(f"Length of our Linked List is {root.get_length_linked_list()}.")
    print(root.reverse_l_list(), "\n")