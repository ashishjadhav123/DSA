
class CNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = CNode(data=data)

        if self.head is None:
            node.next = node
            self.head = node
            return

        itr = self.head
        while itr.next != self.head:
            itr = itr.next

        node.next = self.head
        itr.next = node
        self.head = node

    def print_linked_list(self):

        if self.head is None:
            return "", 0

        itr = self.head
        str_c_list = ""
        counter = 0

        while True:
            str_c_list += str(itr.data)
            counter += 1
            itr = itr.next
            if itr != self.head:
                str_c_list += " ⇄ "
            else:
                break

        return str_c_list, counter


if __name__ == '__main__':
    root = CircularLinkedList()

    root.insert_at_beginning(5)
    root.insert_at_beginning(10)

    print(root.print_linked_list()[0])