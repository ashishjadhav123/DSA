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

    def insert_values(self, data):
        for i in data:
            self.insert_at_end(data=i)

    def insert_after_value(self, data_after, data_to_insert):

        if self.head is None:
            return

        if self.head.data == data_after:
            self.head.next = Node(data=data_to_insert, next=self.head.next)
            return

        itr = self.head

        while itr:
            if str(itr.data) == str(data_after):
                itr.next = Node(data=data_to_insert, next=itr.next)
                break
            itr = itr.next

    def remove_by_value(self, data):

        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return 

        itr = self.head

        while itr:
            if str(itr.next.data) == str(data):
                itr.next = itr.next.next
                break
            itr = itr.next


if __name__ == '__main__':
    root = Singly_linked_list()

    root.insert_values(["banana","mango","grapes","orange"])
    print(root.print_linked_list())

    root.insert_after_value(data_after="mango",data_to_insert="apple")
    print(root.print_linked_list())

    root.remove_by_value(data="mango")
    print(root.print_linked_list())
