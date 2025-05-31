
class DNode:
    def __init__(self, data=None, prv=None, next=None):
        self.data = data
        self.prv = prv
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = DNode(data=data, next=self.head)
        self.head = node

    def print_linked_list(self):

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

        itr = self.head
        counter = 0

        while itr:
            counter += 1
            itr = itr.next

        return counter


    def insert_at_end(self, data):

        if self.head is None:
            self.head = DNode(data=data, next=self.head)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = DNode(data=data, prv=itr)


    def insert_at_loc(self, index, data):
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