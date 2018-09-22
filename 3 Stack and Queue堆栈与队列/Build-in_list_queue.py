'''
使用Python的内建类型list列表实现很方便
'''
class Queue():
    def __init__(self):
        self.items = []
　　
    #增于尾后tail
    def enqueue(self, item):
        self.items.append(item)
    
    #删于头首head
    def dequeue(self):
        return self.items.pop(0)

    def empty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)