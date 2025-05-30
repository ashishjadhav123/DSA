class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Singly_linked_list:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data=data, next=self.head)
        self.head = node


    def insert_at_end(self, data):

        if self.head == None:
            self.head = Node(data=data, next=None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data=data)

    def print_linked_list(self):

        itr = self.head
        l_list_str = ""

        while itr:
            suffix = ''
            if itr.next:
                suffix = '-->'
            l_list_str += str(itr.data) + suffix
            itr = itr.next
        return l_list_str



if __name__ == '__main__':
    root = Singly_linked_list()

    root.insert_at_beginning(5)
    root.insert_at_beginning(10)
    root.insert_at_beginning(15)

    print(root.print_linked_list())

    root.insert_at_end(20)
    root.insert_at_end(25)
    root.insert_at_end(25)

    print(root.print_linked_list())

