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

class ListNode:
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

#####################
#### ROOTED TREES ###
#####################

class BinaryTree:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left 
        self.right = right 
    
    def insert(self, data):
        if self.data:
            if data < self.data :
                if self.left is None:
                    self.left = BinaryTree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BinaryTree(data)
                else:
                    self.right.insert(data)
    
    def get_tree(self):
        if self.left:
            self.left.getTree()
        print(self.data)
        if self.right:
            self.right.get_tree()

# class GenericTree:
#     def __init__(self, data):
#         self.data = data 
#         self.left_child = None 
#         self.right_sibling = None 
    
#     def insert(self, data):
#         if self.data:
#             if self.left_child is None:
#                 self.left = GenericTree(data) 
#             else:




