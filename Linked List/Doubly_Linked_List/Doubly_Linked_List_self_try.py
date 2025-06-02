class DNode:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):

        node = DNode(data=data, next=self.head)

        if self.head is not None:
            self.head.prev = node

        self.head = node

    def print_l_list(self):
        if self.head is None:
            return None, 0

        itr = self.head
        str_l_list = ''
        counter = 0

        while itr:
            suffix = ''
            if itr.next:
                suffix = ' ⇄ '
            # suffix = ' ⇄ ' if itr.next else ''
            str_l_list += str(itr.data) + suffix
            itr = itr.next
            counter += 1

        return str_l_list, counter

    def insert_at_end(self, data):
        if self.head is None:
            self.head = DNode(data=data, next=self.head)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = DNode(data=data, prev=itr)

    def insert_at_loc(self, loc, data):
        if loc < 0 or loc > self.print_l_list()[1]:
            raise Exception("Invalid Index")

        if loc == 0:
            self.insert_at_beginning(data=data)
            return

        itr = self.head
        counter = 0

        while itr:
            if counter == (loc - 1):
                d_node = DNode(data=data, next=itr.next, prev=itr)
                if itr.next:
                    itr.next.prev = d_node
                itr.next = d_node
                break
            counter += 1
            itr = itr.next

    def remove_at_loc(self, loc):
        if loc < 0 or loc > self.print_l_list()[1]:
            raise Exception("Invalid Index")

        if loc == 0:
            if self.head.next:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = None
            return

        itr = self.head
        counter = 0

        while itr:
            if counter == loc:
                if itr.prev:
                    itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break
            counter += 1
            itr = itr.next

    def reverse_l_list(self):
        itr = self.head

        while itr.next:
            itr = itr.next

        reverse_str_l_list = ''
        while itr:
            suffix = ' ⇄ ' if itr.prev else ''
            reverse_str_l_list += str(itr.data) + suffix
            itr = itr.prev

        return reverse_str_l_list


if __name__ == '__main__':
    root = DoublyLinkedList()

    root.insert_at_beginning(5)
    root.insert_at_beginning(10)
    root.insert_at_beginning(15)

    print(root.print_l_list()[0])
    print(f"Length of our Linked List is {root.print_l_list()[1]}.")
    print(root.reverse_l_list(), '\n')

    root.insert_at_end(20)
    root.insert_at_end(25)

    print(root.print_l_list()[0])
    print(f"Length of our Linked List is {root.print_l_list()[1]}.")
    print(root.reverse_l_list(), '\n')

    root.insert_at_loc(loc=2, data=30)
    root.insert_at_loc(loc=6, data=35)

    print(root.print_l_list()[0])
    print(f"Length of our Linked List is {root.print_l_list()[1]}.")
    print(root.reverse_l_list(), '\n')

    root.remove_at_loc(0)
    root.remove_at_loc(3)

    print(root.print_l_list()[0])
    print(f"Length of our Linked List is {root.print_l_list()[1]}.")
    print(root.reverse_l_list(), '\n')

