
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
            self.head.prev = new_node
            self.head = new_node

    def print_l_list(self):

        itr = self.head
        stop_point = self.head
        str_l_list = ''

        while itr.next:
            suffix = ' ⇄ ' if itr.next else ''
            str_l_list += str(itr.data) + suffix
            itr = itr.next

            if itr == stop_point:
                break

        return str_l_list

if __name__ == '__main__':
    root = CircularDoublyLinkedList()

    root.insert_at_beginning(data=5)
    root.insert_at_beginning(data=10)
    root.insert_at_beginning(data=15)

    print(root.print_l_list())