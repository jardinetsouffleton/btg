# stacks are LIFO
class Stack:
    def __init__(self):
        self.contents = []
    
    def push(self, x):
        self.contents.append(x)
    
    def pop(self):
        return self.contents.pop()

# queues are FIFO
class Queue:
    def __init__(self):
        self.contents = []
    
    def enqueue(self, x):
        self.contents.append(x)
    
    def dequeue(self, x):
        return self.contents.popleft()

#####################
#### LINKED LIST ####
#####################

class Node:
    def __init__(self, key):
        self.key = key  
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None 
    
    def insert(self, x):
        x.next = self.head 
        if self.head is not None:
            self.head.prev = x 
        self.head = x
        x.prev = None 

    def search(self, key):
        x = self.head
        while (key is not None) and (x.key != key):
            x = x.next
        return x
    
    def delete(self, x):
        x.prev = x.next
        x.next = x.prev
