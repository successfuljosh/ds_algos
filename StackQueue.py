#STACK is a linear data structure which follows LIFO (Last In First Out)
#QUEUE is a linear data structure which follows FIFO (First In First Out)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    #flows in from the head, leaves through the tail
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        #check if queue is empty, head is the last element in the queue
        return self.head == None

    def peek(self):
        if not self.head == None:
            return self.head.data

    def add(self, data):
        node = Node(data)
        #check if head is empty
        if self.head == None:
            self.head = node
        if self.tail != None:
            self.tail.next = node
        self.tail = node

    def remove(self):
        data = self.head.data
        self.head = self.head.next
        if self.head ==None:
            self.tail==None

        return data




class Stack:
    #flows in from the head, leaves through the head
    def __init__(self):
        self.top = None


    def is_empty(self):
        return self.top == None

    def peek(self):
        if self.top == None:
            return
        return self.top.data

    def push(self, data):
        node = Node(data)
        if self.top == None:
            self.top = node
        node.next = self.top
        self.top = node


    def pop(self):
        if self.top==None:
            return
        data = self.top.data
        self.top = self.top.next

        return data

    def print(self):
        ans = ''
        temp = self.top
        while temp != None:
            ans = ans + ',' + str(temp.data)
            temp = temp.next
        return ans

#Queue Implementation
queue = Queue()
print(queue.is_empty())
queue.add(13)
queue.add(4)
print(queue.peek())
# queue.remove()
print(queue.is_empty())

print('Stack Implementation')
stack = Stack()
print(stack.is_empty())
print(stack.peek())
stack.push(2)
print(stack.peek())
# stack.pop()
print(stack.print())
print(stack.is_empty())