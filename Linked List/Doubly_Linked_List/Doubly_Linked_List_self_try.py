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
        self.head = node

    def print_l_list(self):

        itr = self.head
        str_l_list = ''
        counter = 0

        while itr:
            suffix = ''
            if itr.next:
                suffix = ' ⇄ '
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

        itr.next = DNode(data=data)

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
                itr.next = DNode(data=data, next=itr.next)
                break
            counter += 1
            itr = itr.next

    def remove_at_loc(self, loc):
        if loc < 0 or loc > self.print_l_list()[1]:
            raise Exception("Invalid Index")

        if loc == 0:
            self.head = self.head.next
            return

        itr = self.head
        counter = 0

        while itr:
            if counter == (loc - 1):
                itr.next = itr.next.next
                break
            counter += 1
            itr = itr.next


if __name__ == '__main__':
    rooot = DoublyLinkedList()

    rooot.insert_at_beginning(5)
    rooot.insert_at_beginning(10)
    rooot.insert_at_beginning(15)

    print(rooot.print_l_list()[0])

    rooot.insert_at_end(20)
    rooot.insert_at_end(25)

    print(rooot.print_l_list()[0])

    rooot.insert_at_loc(loc=2, data=30)

    print(rooot.print_l_list()[0])

    rooot.remove_at_loc(0)

    print(rooot.print_l_list()[0])

