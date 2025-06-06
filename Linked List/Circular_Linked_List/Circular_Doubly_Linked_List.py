
class CDNode:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = CDNode(data=data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            tail = self.head.prev

            new_node.next = self.head
            new_node.prev = tail

            tail.next = new_node
            self.head.prev = new_node   # Here current self.head prev
            self.head = new_node        # Here we assign new_node to self.head

    def insert_at_end(self, data):
        new_node = CDNode(data=data)
        tail = self.head.prev
        head = self.head

        itr = self.head

        while itr.next:
            itr = itr.next

            if itr == tail:
                break

        itr.next = new_node
        new_node.prev = itr
        new_node.next = head

    def print_l_list(self):

        itr = self.head
        stop_point = self.head
        str_l_list = ''
        counter = 0

        while itr.next:
            suffix = ' ⇄ ' if itr.next else ''
            str_l_list += str(itr.data) + suffix
            itr = itr.next
            counter += 1

            if itr == stop_point:
                break

        return str_l_list,counter

    def insert_at_loc(self, loc, data):
        if loc < 0 or loc > (self.print_l_list()[1]):
            raise Exception("Enter valid Loc")

        if loc == 0:
            self.insert_at_beginning(data=data)
            return

        new_node = CDNode(data=data)
        itr = self.head
        counter = 0

        while itr:
            if counter == (loc - 1):

                new_node.prev = itr
                new_node.next = itr.next

                itr.next.prev = new_node
                itr.next = new_node
                break
            counter += 1
            itr = itr.next

    def remove_at_loc(self, loc):

        if loc == 0:
            tail = self.head.prev
            self.head = self.head.next
            self.head.prev = tail
            tail.next = self.head
            return

        itr = self.head
        counter = 0

        while itr:
            if counter == (loc - 1):
                itr.next = itr.next.next
                itr.next.next.prev = itr
                break
            counter += 1
            itr = itr.next


if __name__ == '__main__':
    root = CircularDoublyLinkedList()

    root.insert_at_beginning(data=5)
    root.insert_at_beginning(data=10)
    root.insert_at_beginning(data=15)

    print(root.print_l_list()[0])

    root.insert_at_end(data=20)

    print(root.print_l_list()[0])

    root.insert_at_loc(loc=2, data=30)
    root.insert_at_loc(loc=5, data=35)
    root.insert_at_loc(loc=0, data=40)

    print(root.print_l_list()[0])

    root.remove_at_loc(loc=0)

    print(root.print_l_list()[0])