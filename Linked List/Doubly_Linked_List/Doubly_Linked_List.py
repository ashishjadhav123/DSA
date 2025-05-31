
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

    def insert_at_end(self, data):

        if self.head is None:
            self.head = DNode(data=data, next=self.head)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = DNode(data=data, prv=itr)


if __name__ == '__main__':
    root = DoublyLinkedList()

    root.insert_at_beginning(5)
    root.insert_at_beginning(10)

    print(root.print_linked_list())

    root.insert_at_end(15)
    root.insert_at_end(20)

    print(root.print_linked_list())