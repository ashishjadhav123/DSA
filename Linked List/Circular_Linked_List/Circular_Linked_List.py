
class CNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """Method to insert element at beginning of Linked List"""
        if self.head is None:
            self.head = CNode(data=data, next=self.head)
        else:
            self.head = CNode(data=data, next=self.head)

            itr = self.head

            while itr.next:
                itr = itr.next

            itr.next = self.head

    def print_l_list(self):
        """Method for print all elements from Linked List"""
        itr = self.head
        stop_point = self.head
        counter = 0
        str_l_list = ''
        while itr:
            suffix = ' -> ' if itr.next else ''
            str_l_list += str(itr.data) + suffix
            itr = itr.next
            counter += 1
            if itr == stop_point:
                break

        return str_l_list, counter

    def insert_at_end(self, data):
        """Method to insert element at end of Linked List"""
        if self.head is None:
            self.insert_at_beginning(data=data)
            return

        itr = self.head
        stop_point = self.head

        while itr.next:
            itr = itr.next
            if itr.next == stop_point:
                break

        itr.next = CNode(data=data, next=self.head)

    def insert_at_loc(self, loc, data):
        """Method to insert element at specific index of Linked List"""
        if loc < 0 or loc > (self.print_l_list()[1]):
            raise Exception("Invalid loc")

        if loc == 0:
            self.insert_at_beginning(data=data)
            return

        itr = self.head
        counter = 0
        while itr:
            if counter == (loc - 1):
                itr.next = CNode(data=data, next=itr.next)
                break
            counter += 1
            itr = itr.next

    def remove_at_loc(self, loc):
        """Method to remove element at specific Location of Linked List"""
        if loc < 0 or loc > (self.print_l_list()[1]):
            raise Exception("Invalid loc")

        if loc == 0:

            itr = self.head
            stop_point = self.head

            self.head = self.head.next

            while itr.next:
                itr = itr.next
                if itr.next == stop_point:
                    break

            itr.next = self.head
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
    root = CircularLinkedList()

    root.insert_at_beginning(5)
    root.insert_at_beginning(10)

    print(root.print_l_list()[0])
    print(f"Length of Circular Linked list : {root.print_l_list()[1]}")

    root.insert_at_end(15)
    root.insert_at_end(20)

    print(root.print_l_list()[0])
    print(f"Length of Circular Linked list : {root.print_l_list()[1]}")

    root.insert_at_loc(loc=2, data=25)
    root.insert_at_loc(loc=5, data=30)

    print(root.print_l_list()[0])
    print(f"Length of Circular Linked list : {root.print_l_list()[1]}")

    root.remove_at_loc(loc=2)

    print(root.print_l_list()[0])
    print(f"Length of Circular Linked list : {root.print_l_list()[1]}")

    root.remove_at_loc(loc=0)

    print(root.print_l_list()[0])
    print(f"Length of Circular Linked list : {root.print_l_list()[1]}")

    root.insert_at_loc(loc=2, data=35)

    print(root.print_l_list()[0])
    print(f"Length of Circular Linked list : {root.print_l_list()[1]}")
