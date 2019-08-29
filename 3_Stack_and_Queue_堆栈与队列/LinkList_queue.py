'''
链表
模块方法来自链表笔记代码
'''
from LinkedList import LinkedList
from LinkedList import Node

class LinkedQueue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0  
    
    # O(1)
    def enqueue(self, value):
        new_node = Node(value)

        if self.tail is not None:
            self.tail.next = new_node

        else:
            self.head = new_node

        self.tail = new_node
        self.count += 1
    
    # O(1)
    def dequeue(self):
        if not self.is_empty():
            # print head to next node
            tmp = self.head
            self.head = self.head.next
            print("dequeue sucess")
            self.count -= 1
            return tmp
        else:
            raise ValueError("Empty QUEUE")

    def is_empty(self):
        if self.head is None and self.tail is None:
            return True
        else:
            return False

    def peek(self):
        return self.head.data

        
    def __len__(self):
        return self.count    

    def is_empty(self):
        return self.count == 0
    
    def print(self):
        node = self.head
        while node:
            print(node.value, end = " ")
            node = node.next
        print('')        