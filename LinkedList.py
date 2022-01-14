# Linked list is a sequence of data strutures with connection/link to its next node.
# linked list with forward and backward connections is call DOUBLY LINKED LIST

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if (self.head == None):
            self.head = Node(data)
            self.print()
            return

        current = self.head
        while (current.next != None):
            current = current.next
        current.next = Node(data)
        self.print()

    # inserting data behind the head (as the first item on the list)
    def prepend(self, data):
        #check if head is not null
        if (self.head == None):
            self.head = Node(data)
            self.print()
            return
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head
        self.print()

    def delete(self, data):
        if self.head == None:
            return
#remove head if dat matches
        if self.head.data == data:
            self.head = self.head.next
            self.print()
            return

        current = self.head
        while current.next != None:
            if current.next.data == data:
                current.next = current.next.next
                self.print()
                return
            current = current.next


    def print(self):
        current = self.head
        text = ''
        while current != None:
            text += str(current.data) +', '
            current = current.next
        print(text)


if __name__== '__main__':
    my_list = LinkedList()
    my_list.append(2)
    my_list.append(3)
    my_list.prepend(3)
    my_list.delete(2)
