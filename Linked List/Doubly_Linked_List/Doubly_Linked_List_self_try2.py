
class DNode:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):

        dnode = DNode(data=data, next=self.head)

        if self.head is not None:
            self.head.prev = dnode

        self.head = dnode


    def print_l_list(self):
        if self.head is None:
            return None, 0

        itr = self.head
        counter = 0
        str_l_list = ""
        while itr:
            suffix = " ⇄ " if itr.next else ""
            str_l_list += str(itr.data) + suffix
            counter += 1
            itr = itr.next

        return str_l_list, counter

    def reverse_l_list(self):

        itr = self.head

        while itr.next:
            itr = itr.next

        str_l_list = ""

        while itr:
            suffix = " ⇄ " if itr.prev else ""
            str_l_list += str(itr.data) + suffix
            itr = itr.prev

        return str_l_list

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
                if itr.next:
                    itr.next.prev = DNode(data=data, next=itr.next, prev=itr)
                itr.next = DNode(data=data, next=itr.next, prev=itr)
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
                if itr.next:
                    itr.next.prev = itr.prev
                if itr.prev:
                    itr.prev.next = itr.next
            counter += 1
            itr = itr.next

    def merge_d_linked_list(self, list1, list2):

        if list1.head is None:
            list1.head = list2.head
            return list1

        if list2.head is None:
            return list1

        itr = list1.head

        while itr.next:
            itr = itr.next

        itr.next = list2.head
        list2.head.prev = itr

        return list1



if __name__ == '__main__':

    root = DoublyLinkedList()

    root.insert_at_beginning(15)
    root.insert_at_beginning(10)
    root.insert_at_beginning(5)

    print(root.print_l_list()[0])
    print(root.reverse_l_list())

    root.insert_at_end(20)
    root.insert_at_end(25)

    print(root.print_l_list()[0])
    print(root.reverse_l_list())

    root.insert_at_loc(loc=2, data=55)

    print(root.print_l_list()[0])
    print(root.reverse_l_list())

    root.remove_at_loc(loc=2)

    print(root.print_l_list()[0])
    print(root.reverse_l_list())

    root2 = DoublyLinkedList()

    root2.insert_at_beginning(95)
    root2.insert_at_beginning(85)

    root.merge_d_linked_list(list1=root, list2=root2)
    print(root.print_l_list()[0])